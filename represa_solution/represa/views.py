from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader
from django.template import RequestContext
import json as simplejson
import urllib2 


def get_url():
  return ("https://sabesp-api.herokuapp.com/")


def fetch_and_draw_data(request):
	data_url = get_url()
	response = urllib2.urlopen (data_url)
	jsonData = simplejson.load(response)
	return HttpResponse(simplejson.dumps(jsonData), mimetype='application/json')
# Create your views here.

def index(request):
  template = loader.get_template('represa/index.html')
  context = RequestContext(request)
  return HttpResponse(template.render(context))