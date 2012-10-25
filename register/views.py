# Create your views here.
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def home(request):
	return render_to_response("home/base.html",{})