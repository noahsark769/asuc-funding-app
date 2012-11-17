from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return render_to_response("base.html",
		{'name':"Shitface Mcgee", 'is_admin': True},
		context_instance=RequestContext(request))