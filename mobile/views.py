# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging

def hello(request):
    return render(request,'index.html', {'content': 'Welcome to a jQueryMobile page'}) 

def home(request):
    return render(request, 'home.html', {'content': 'This could be dynamic!'}) 

def discover(request):
    return render(request, 'discover.html')

def me(request):
    return render(request, 'me.html')
