from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse

import ldap
import xml.dom.minidom
import urllib2

from funding_app.models import *

# Authentication

def calnet_login_url():
	return "https://auth-test.berkeley.edu/cas/login?service=http://localhost:8000/process_calnet/"

def calnet_validation_url(request):
	return "https://auth-test.berkeley.edu/cas/serviceValidate?ticket=" + request.GET.get('ticket') + "&service=http://localhost:8000/process_calnet/"

def calnet_logout_url():
	return "https://auth-test.berkeley.edu/cas/logout"

def check_credentials(request):
	if request.COOKIES.has_key('uid'):
		return True
	else:
		return False

def get_credentials(request):
	return {'uid': request.COOKIES['uid'], 'name': request.COOKIES['name'], 'phone': request.COOKIES['phone'], 'email': request.COOKIES['email']}

def is_admin(request):
	c = Config.objects.all()[0]
	try:
		admin = c.configadmin_set.get(email=get_credentials(request)['email'])
		return True
	except ObjectDoesNotExist as e:
		return False

def process_calnet(request):
	if request.method != 'GET' or request.GET.get('ticket') is None:
		return redirect(calnet_login_url())

	f = urllib2.urlopen(calnet_validation_url(request))
	doc = xml.dom.minidom.parse(f)
	if len(doc.documentElement.getElementsByTagName('cas:authenticationSuccess')) == 0:
		return redirect(calnet_login_url())

	uid = int(doc.documentElement.getElementsByTagName('cas:user')[0].firstChild.nodeValue)
	l = ldap.open("ldap.berkeley.edu")
	l.simple_bind_s('', '') # no credentials needed for anonymous bind
	result_id = l.search("ou=people,dc=berkeley,dc=edu", ldap.SCOPE_SUBTREE, "uid=" + str(uid), None)
	data = l.result(result_id, 0)[1][0][1]

	response = redirect('funding_app.views.home')
	response.set_cookie('uid', str(uid), max_age=None)
	response.set_cookie('name', data['displayName'][0].title(), max_age=None)
	if data.get('telephoneNumber') is not None:
		response.set_cookie('phone', convert_phone(data.get('telephoneNumber')[0]), max_age=None)
	else:
		response.set_cookie('phone', '', max_age=None)
	response.set_cookie('email', data['mail'][0], max_age=None)

	return response

def logout(request):
	response = redirect(calnet_logout_url())
	response.delete_cookie('uid')
	response.delete_cookie('name')
	response.delete_cookie('phone')
	response.delete_cookie('email')
	return response

def convert_phone(phone):
	return phone[3:6] + "-" + phone[7:15]

# Views

def home(request):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())

	if is_admin(request) == True:
		return redirect('funding_app.views.admin_request_summary')
	else:
		return redirect('funding_app.views.submitter_request_summary')

# Admin Views

def admin_request_summary(request):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	""" Returns a list of all funding requests, item by item.

	The following fields are included:
		- Request ID (pk)
		- Date Submitted
		- Request Status
		- Student Group
		- Request Type
		- Request Category
		- Request For (Event, OC)
		- Funding Round
		- Total Requested
		- Total Awarded
	"""
	user = get_credentials(request)

	try:
		fundingRequests = FundingRequest.objects.all()
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("admin_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def admin_render_funding_request(request, request_id):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	user = get_credentials(request)

	try:
		fundingRequest = GraduateRequest.objects.get(id=request_id)
	except ObjectDoesNotExist as e:
		try:
			fundingRequest = UndergraduateRequest.objects.get(id=request_id)
		except ObjectDoesNotExist as e:
			fundingRequest = TravelRequest.objects.get(id=request_id)

	if fundingRequest.requestStatus == "Awarded":
		url = "admin_review.html"
	else:
		url = "admin_award.html"

	return render_to_response(url, {'funding_request': fundingRequest, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def config(request):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	user = get_credentials(request)
	c = Config.objects.all()[0]

	admins = c.configadmin_set.all()
	locations = c.configlocation_set.all()
	ug_req_cats = c.configugreqcat_set.all()
	grad_req_cats = c.configgradreqcat_set.all()
	ug_grant_cats = c.configuggrant_set.all()
	grad_grant_cats = c.configgradgrant_set.all()
	funding_rounds = c.configfundinground_set.all()
	grad_delegates = c.configgraddelegate_set.all()

	return render_to_response("config.html",{
		'admins': admins,
		'locations': locations,
		'ug_req_cats': ug_req_cats,
		'grad_req_cats': grad_req_cats,
		'ug_grant_cats': ug_grant_cats,
		'grad_grant_cats': grad_grant_cats,
		'funding_rounds': funding_rounds,
		'grad_delegates': grad_delegates,
		'name': user['name'], 'is_admin': is_admin(request)
		}, context_instance=RequestContext(request))

# Submitter Views

def submitter_request_summary(request):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())

	""" Returns a list of the submitter's funding requests, item by item.

	The following fields are included:
		- Request ID
		- Date Submitted
		- Request Status
		- Student Group
		- Request Type
		- Request Category
		- Request For (Event, OC)
		- Funding Round
		- Total Requested
		- Total Awarded
	"""
	user = get_credentials(request)

	try:
		fundingRequests = FundingRequest.objects.filter(uid=user['uid'])
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("submitter_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def submitter_render_funding_request(request, request_id):
	if check_credentials(request) == False:
		return redirect(calnet_login_url())

	try:
		fundingRequest = GraduateRequest.objects.get(id=request_id)
	except ObjectDoesNotExist as e:
		try:
			fundingRequest = UndergraduateRequest.objects.get(id=request_id)
		except ObjectDoesNotExist as e:
			fundingRequest = TravelRequest.objects.get(id=request_id)

	if fundingRequest.requestStatus == "Submitted":
		url = "submitter_review.html"
	else:
		url = "submitter_create.html"

	return render_to_response(url, {'funding_request': fundingRequest, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def email_delegate(request_id):
	try:
		graduateRequest = GraduateRequest.objects.get(id=request_id)
	except:
		return

	subject = 'New GA Funding Request for ' + graduateRequest.studentGroup
	message = """A new graduate request has been submitted for the graduate assembly:

	Request ID:\t\t\t""" + str(graduateRequest.id) + """
	Date Submitted:\t\t\t""" + str(graduateRequest.dateSubmitted) + """
	Requested By:\t\t\t""" + graduateRequest.name + """
	Sponsoring Student Group:\t\t\t""" + graduateRequest.studentGroup + """
	Request Category\t\t\t""" + graduateRequest.requestCategory + """
	Funding Round\t\t\t""" + graduateRequest.fundingRound + """
	Total Requested\t\t\t""" + str(graduateRequest.compute_requested_total()) + """

	Click or copy/paste this link to review the request: {insert link}
	Click or copy/paste this link to review ALL requests: {insert link}
	"""

	send_mail(subject, message, 'no-reply@berkeley.edu', ['aiyengar@berkeley.edu'], fail_silently=False)

# EOF
