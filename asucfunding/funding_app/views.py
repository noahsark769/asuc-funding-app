from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
import ldap

from funding_app.models import *

# Miscellaneous

def get_credentials():
	uid = 6081

	l = ldap.open("ldap.berkeley.edu")
	l.simple_bind_s('', '') # no credentials needed for anonymous bind
	result_id = l.search("ou=people,dc=berkeley,dc=edu", ldap.SCOPE_SUBTREE, "uid=" + str(uid), None)
	data = l.result(result_id, 0)[1][0][1]
	return {'uid': uid, 'name':data['displayName'][0].title(), 'phone': convert_phone(data['telephoneNumber'][0]), 'email': data['mail'][0]}

def convert_phone(phone):
	return phone[3:6] + "-" + phone[7:15]

def is_admin():
	c = Config.objects.all()[0]
	try:
		admin = c.configadmin_set.get(email=get_credentials()['email'])
		return True
	except ObjectDoesNotExist as e:
		return False

def home(request):
	return render_to_response("admin_request_summary.html",
		{'name':"Shitface Mcgee", 'is_admin': True, "funding_requests": FundingRequest.objects.all()},
		context_instance=RequestContext(request))

# Admin Views

def admin_request_summary(request):
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
	user = get_credentials()

	try:
		fundingRequests = FundingRequest.objects.all()
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("admin_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin()}, context_instance=RequestContext(request))

def admin_render_funding_request(request, request_id):
	user = get_credentials()

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

	return render_to_response(url, {'funding_request': fundingRequest, 'name': user['name'], 'is_admin': user['is_admin']}, context_instance=RequestContext(request))

def config(request):
	c = Config.objects.all()[0]

	admins = c.configadmin_set.all()
	locations = c.configlocation_set.all()
	ug_req_cats = c.configugreqcat_set.all()
	grad_req_cats = c.configgradreqcat_set.all()
	ug_grant_cats = c.configuggrantcat_set.all()
	grad_grant_cats = c.configgradgrantcat_set.all()
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
		'name': user['name'], 'is_admin': user['is_admin']
		}, context_instance=RequestContext(request))

# Submitter Views

def submitter_request_summary(request):
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
	user = get_credentials()

	try:
		fundingRequests = FundingRequest.objects.filter(uid=user['uid'])
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("submitter_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin()}, context_instance=RequestContext(request))

def submitter_render_funding_request(request, request_id):
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

	return render_to_response(url, {'funding_request': fundingRequest, 'name': user['name'], 'is_admin': user['is_admin']}, context_instance=RequestContext(request))

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

	#send_mail(subject, message, 'no-reply@berkeley.edu', [graduateRequest.gaDelegate], fail_silently=False)
	send_mail(subject, message, 'no-reply@berkeley.edu', ['aiyengar@berkeley.edu'], fail_silently=False)

# Other Views

def calnet_auth():
	

# EOF
