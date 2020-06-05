from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from returngender import returngender
from returnprobability import returnprobability
# Create your views here.
def home(request):
	return HttpResponse("Hello Hemant world")
def hello(request):
	name=request.GET["name"]
	return HttpResponse(name)
def genderapi(request):
	c=request.GET["name"]
	gender=returngender(c)
	probability=returnprobability(c)
	data = [{'Gender': gender},	{'Probability': probability}]
	return JsonResponse(data,safe=False)