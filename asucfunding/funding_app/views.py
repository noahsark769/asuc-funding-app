from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from funding_app.models import *

def get_credentials():
	return {'uid': 23621811, 'name':'Shitface Mcgee', 'phone': '5109999999', 'email': 'shitface@mcgee.biz'}

def is_admin():
	c = Config.objects.all()[0]
	try:
		admin = c.configadmin_set.get(get_credentials['email']=email)
		return True
	except ObjectDoesNotExist as e:
		return False

def home(request):
	return render_to_response("base.html",
		{'name':"Shitface Mcgee", 'is_admin': True},
		context_instance=RequestContext(request))

# Admin Views

def admin_request_summary(request):
	""" Returns a list of funding requests, item by item.
	If you are an admin, returns all requests.
	If you are a submitter, returns only your requests.

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
		fundingRequests = FundingRequest.objects.all()
	except ObjectDoesNotExist as e:
		fundingRequests = []

	for fundingRequest in fundingRequests:
		reqestedTotal = 0
		awardedTotal = 0
		for event in fundingRequest.event_set.all():
			requestedTotal += event.budget.requestedTotal
			awardedTotal += event.budget.awardedTotal

		fundingRequest['requestedTotal'] = requestedTotal
		fundingRequest['awardedTotal'] = awardedTotal

	return render_to_response("admin_request_summary.html", {'funding_requests': fundingRequests, 'is_admin': is_admin()})

def submitter_request_summary(request):
	""" Returns a list of funding requests, item by item.
	If you are an admin, returns all requests.
	If you are a submitter, returns only your requests.

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
		fundingRequests = FundingRequest.objects.get(uid=user['uid'])
	except ObjectDoesNotExist as e:
		fundingRequests = []

	for fundingRequest in fundingRequests:
		reqestedTotal = 0
		awardedTotal = 0
		for event in fundingRequest.event_set.all():
			requestedTotal += event.budget.requestedTotal
			awardedTotal += event.budget.awardedTotal

		fundingRequest['requestedTotal'] = requestedTotal
		fundingRequest['awardedTotal'] = awardedTotal

	return render_to_response("submitter_request_summary.html", {'funding_requests': fundingRequests, 'is_admin': is_admin()})

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
		})

def render_funding_request(request, request_id):
	try:
		fundingRequest = GraduateRequest.objects.get(pk=request_id)
	except ObjectDoesNotExist as e:
		try:
			fundingRequest = UndergraduateRequest.objects.get(pk=request_id)
		except ObjectDoesNotExist as e:
			fundingRequest = TravelRequest.objects.get(pk=request_id

	if is_admin():
		if fundingRequest.requestStatus == "Awarded":
			url = "admin_review.html"
		else:
			url = "admin_award.html"
	else:
		if fundingRequest.requestStatus == "Saved":
			url = ""

	return render_to_response("", fundingRequest)

# Submitter Views
