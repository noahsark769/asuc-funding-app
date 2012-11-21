from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse
import ldap
from datetime import date
from cgi import escape

import xml.dom.minidom
import urllib2

from funding_app.models import *

## Constants
CONFIG_KEY_CLASS_MAP = { 'admin_roster': ConfigAdmin,
						'event_locations': ConfigLocation,
						'ug_request_categories': ConfigUGReqCat,
						'grad_request_categories': ConfigGradReqCat,
						'ug_grant_categories': ConfigUGGrant,
						'grad_grant_categories': ConfigGradGrant,
						'funding_rounds': ConfigFundingRound,
						'delegates': ConfigGradDelegate }

CONFIG_KEY_ID_MAP = { 'admin_roster': 'admin_email',
						'event_locations': 'location',
						'ug_request_categories': 'ug_req_cat',
						'grad_request_categories': 'grad_req_cat',
						'ug_grant_categories': 'ug_grant_cat',
						'grad_grant_categories': 'grad_grant_cat',
						'funding_rounds': 'round',
						'delegates': 'delegate' }

CONFIG_KEY_PARAM_MAP = { 'admin_roster': 'email',
						'event_locations': 'location',
						'ug_request_categories': 'category',
						'grad_request_categories': 'category',
						'ug_grant_categories': 'category',
						'grad_grant_categories': 'category'}

# Authentication

def calnet_login_url():
	"""
	Return the CalNet authentication URL.
	"""
	return "https://auth-test.berkeley.edu/cas/login?service=http://localhost:8000/process_calnet/"

def calnet_validation_url(request):
	"""
	Return the validation URL for CalNet authentication tickets.
	"""
	return "https://auth-test.berkeley.edu/cas/serviceValidate?ticket=" + request.GET.get('ticket') + "&service=http://localhost:8000/process_calnet/"

def calnet_logout_url():
	"""
	Return the URL to log out of CalNet.
	"""
	return "https://auth-test.berkeley.edu/cas/logout"

def check_credentials(request):
	"""
	Check whether the user currently has the proper credentials to be logged in (should have authZ and authN).
	"""
	if request.COOKIES.has_key('uid'):
		return True
	else:
		return False

def get_credentials(request):
	"""
	Grab the user's credentials from the cookies, assuming they are properly logged in.
	"""
	return {'uid': request.COOKIES['uid'], 'name': request.COOKIES['name'], 'phone': request.COOKIES['phone'], 'email': request.COOKIES['email']}

def is_admin(request):
	"""
	Check whether a user is an administrator by comparing their e-mail address with the admin roster.
	"""
	try:
		admin = ConfigAdmin.objects.get(email=get_credentials(request)['email'])
		return True
	except ObjectDoesNotExist as e:
		return False

def process_calnet(request):
	"""
	Process the data given to us by CalNet authentication and log the user in.
	This view method will complete only if the user's ticket is properly validated.
	Otherwise, they will be continuously redirected to the CalNet login page.
	"""

	# If there's no ticket given to us, redirect them to the login page
	if request.method != 'GET' or request.GET.get('ticket') is None:
		return redirect(calnet_login_url())

	# Check the ticket. If it's invalid, login page.
	f = urllib2.urlopen(calnet_validation_url(request))
	doc = xml.dom.minidom.parse(f)
	if len(doc.documentElement.getElementsByTagName('cas:authenticationSuccess')) == 0:
		return redirect(calnet_login_url())

	# At this point we're good. extract the user data from LDAP
	uid = int(doc.documentElement.getElementsByTagName('cas:user')[0].firstChild.nodeValue)
	l = ldap.open("ldap.berkeley.edu")
	l.simple_bind_s('', '') # no credentials needed for anonymous bind
	result_id = l.search("ou=people,dc=berkeley,dc=edu", ldap.SCOPE_SUBTREE, "uid=" + str(uid), None)
	data = l.result(result_id, 0)[1][0][1]

	# Set all the appropriate cookies, and take the user home!
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
	"""
	Log the user out by destroying the cookies, then logging out of CalNet.
	"""
	response = redirect(calnet_logout_url())
	response.delete_cookie('uid')
	response.delete_cookie('name')
	response.delete_cookie('phone')
	response.delete_cookie('email')
	return response

def convert_phone(phone):
	"""
	Convert from LDAP phone number format to normal format:
	ex. "+1 ABC DEF-GHIJ" ==> "ABC-DEF-GHIJ".
	"""
	return phone[3:6] + "-" + phone[7:15]

# Views

def home(request):
	"""
	View:

	Redirect to either submitter or admin request log, depending on user credentials.
	"""
	if check_credentials(request) == False:
		return redirect(calnet_login_url())

	if is_admin(request) == True:
		return redirect('funding_app.views.admin_request_summary')
	else:
		return redirect('funding_app.views.submitter_request_summary')

# Admin Views

def admin_request_summary(request):
	"""
	Admin View:

	Show a table containing every request in the system.
	"""
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	user = get_credentials(request)

	try:
		fundingRequests = FundingRequest.objects.all()
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("admin_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def admin_render_funding_request(request, request_id):
	"""
	Admin View:

	Deliver all information about a funding request to the view.
	This is used for the "Admin Review" and "Admin Award" pages.
	"""
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
	"""
	Admin View:

	Return all configuration parameters for the configuration page.
	"""
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	user = get_credentials(request)

	admins = ConfigAdmin.objects.all()
	locations = ConfigLocation.objects.all()
	ug_req_cats = ConfigUGReqCat.objects.all()
	grad_req_cats = ConfigGradReqCat.objects.all()
	ug_grant_cats = ConfigUGGrant.objects.all()
	grad_grant_cats = ConfigGradGrant.objects.all()
	funding_rounds = ConfigFundingRound.objects.all()
	grad_delegates = ConfigGradDelegate.objects.all()

	return render_to_response("config.html",{
		'admins': admins,
		'locations': locations,
		'ug_req_cats': ug_req_cats,
		'grad_req_cats': grad_req_cats,
		'ug_grant_cats': ug_grant_cats,
		'grad_grant_cats': grad_grant_cats,
		'funding_rounds': funding_rounds,
		'grad_delegates': grad_delegates,
		'name': user['name'], 'is_admin': is_admin(request),
		'email': user['email']
		}, context_instance=RequestContext(request))

def change_config(request):
	"""
	Admin View:

	Process adding/removing values from the various tables in the config page.
	"""
	if check_credentials(request) == False:
		return redirect(calnet_login_url())
	if is_admin(request) == False:
		return redirect('funding_app.views.home')

	# DELETING VALUES
	if request.method == 'POST' and request.POST.get('id') and request.POST.get('remove') and request.POST.get('config_key'):
		# select the proper table to delete from
		config_key = request.POST.get('config_key')
		cls = CONFIG_KEY_CLASS_MAP[config_key]

		if config_key == 'admin_roster':
			user = ConfigAdmin.objects.get(id=int(request.POST.get('id')))
			if user is not None and user.id == ConfigAdmin.objects.get(email=get_credentials(request).get('email')).id:
				return HttpResponse('FAILURE')

		# delete the item with the proper id from the table
		cls.objects.filter(id=int(request.POST.get('id'))).delete()

		return HttpResponse('SUCCESS')

	# ADDING VALUES	
	elif request.method == 'POST' and request.POST.get('config_key') is not None:
		# which table we're pulling from 
		config_key = request.POST.get('config_key')
		# cls = CONFIG_KEY_CLASS_MAP[config_key] #we can possible use this here too?

		# the 1-2 input value(s), depending on which field we're editing.
		value1 = request.POST.get('value1')
		value2 = request.POST.get('value2')

		# if value1 is empty, then no data has been passed. this is bad.
		if value1 is None:
			return HttpResponse('FAILURE')

		# it's repeated so much...
		remove_html = '<a class="config_remove" href="">x</a></li>'
		config_class = CONFIG_KEY_ID_MAP[config_key]

		# in this case, we must be choosing between one of the 1-parameter options
		if value2 is None:
			if CONFIG_KEY_CLASS_MAP.get(config_key) is not None:
				print 'got here'
				o = CONFIG_KEY_CLASS_MAP[config_key].objects.create(**{CONFIG_KEY_PARAM_MAP[config_key]: value1})
				return HttpResponse('<li id="' + config_class + '_'+ str(o.id) +'">' + escape(value1) + remove_html)

			else:
				# if it's none of the above, then fail
				return HttpResponse('FAILURE')

		# in this case, we must be choosing between one of the 2-parameter options
		if config_key == 'funding_rounds':
			if value2:
				partitions = value2.split('/')
				months, days, years = partitions[0], partitions[1], partitions[2]
				try:
					this_date = date(int(years), int(months), int(days))
				except Exception as e:
					return HttpResponse('FAILURE')
			else:
				this_date = None

			if this_date:
				o = ConfigFundingRound.objects.create(name=value1, deadline=this_date)
				return HttpResponse('<li id="' + CONFIG_KEY_ID_MAP[config_key] + '_' + str(o.id) +'">' + value1 +'&nbsp;' + this_date.strftime("%b. %d, %Y") + remove_html)
			else:
				return HttpResponse('FAILURE')
		elif config_key == 'delegates':
			o = ConfigGradDelegate.objects.create(name=value1, email=value2)
			return HttpResponse('<li id="' + CONFIG_KEY_ID_MAP[config_key] + '_' + str(o.id) +'">' + value1 +'&nbsp;' + value2 + remove_html)
		else: # well, this should never happen.
			return HttpResponse('FAILURE')
	else:
		return HttpResponse('FAILURE')

# Submitter Views

def submitter_request_summary(request):
	"""
	Submitter View:

	Show a table containing every request in the system.
	"""
	if check_credentials(request) == False:
		return redirect(calnet_login_url())

	user = get_credentials(request)

	try:
		fundingRequests = FundingRequest.objects.filter(uid=user['uid'])
	except ObjectDoesNotExist as e:
		fundingRequests = []

	return render_to_response("submitter_request_summary.html", {'funding_requests': fundingRequests, 'name': user['name'], 'is_admin': is_admin(request)}, context_instance=RequestContext(request))

def submitter_render_funding_request(request, request_id):
	"""
	Submitter View:

	Deliver all information about a funding request to the view.
	This is used for the "New Request" and "Review Request" pages.
	"""
	
	### should the request_id be passed in as a post parameter in request?
	
	
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
	"""
	E-mail the graduate delegate the submitted request, IF the request is a graduate request.
	"""
	try:
		graduateRequest = GraduateRequest.objects.get(id=request_id)
	except ObjectDoesNotExist:
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
