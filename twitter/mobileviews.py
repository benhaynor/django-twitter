# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging
from twitter.forms import *

def hello(request):
    return render(request,'mobile/index.html', {'content': 'Welcome to a jQueryMobile page'}) 

def home(request):
    return render(request, 'mobile/home.html', {'content': 'This could be dynamic!'}) 

def discover(request):
    return render(request, 'mobile/discover.html')

def me(request):
    return render(request, 'mobile/me.html')

def newtweet(request):
    return render(request, 'mobile/newtweet.html')
