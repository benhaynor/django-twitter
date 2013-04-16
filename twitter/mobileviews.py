# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging
import twitter.views 

def main(request):
    if request.is_ajax():
        return home(request)
    else:
        if request.user.is_authenticated():
            return render(request,'mobile/index_signed_in.html')
        else:
            return render(request,'mobile/index.html')

def home(request):
    if request.method == 'POST':
        return twitter.views.landing_page(request)
    else:
        if request.user.is_authenticated():
            return render(request, 'mobile/home.html')
        else:
            return render(request, 'mobile/login.html')

def discover(request):
    return render(request, 'mobile/discover.html')

def me(request):
    return render(request, 'mobile/me.html')

def newtweet(request):
    return render(request, 'mobile/newtweet.html')

def sign_in_success(request):
    return render(request, 'mobile/sign_in_success.html')

def sign_up_success(request):
    return render(request, 'mobile/sign_up_success.html')
