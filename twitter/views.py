from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib import auth
from twitter.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from twitter.models import Tweeter, Tweet
import twitter.forms as twitterforms 
from twitter.serializers import TweetSerializer
from rest_framework import serializers, generics
MOBILE_ROOT = '/mobile'

def landing_page(request):
    if request.is_ajax():
        prefix = MOBILE_ROOT
    else:
        prefix = ''
    if request.user.is_authenticated():
        return profile_page(request)
    if request.method == 'POST':
        post_action = request.POST.get('post_action','')
        if post_action == 'sign_up':
            sign_up_form = UserCreationForm(request.POST)
            if sign_up_form.is_valid():
                sign_up_form.save()
                user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
                auth.login(request,user)
                return HttpResponseRedirect(prefix + '/')

        elif post_action == 'sign_in':
            sign_in_form = twitterforms.SignInForm(request.POST)
            if sign_in_form.is_valid():
                user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
                auth.login(request,user)
                return HttpResponseRedirect(prefix + "/") 

    #Get, and bad unsuccesful login, signup 
    if not 'sign_up_form' in locals():
        sign_up_form = UserCreationForm()
    if not 'sign_in_form' in locals():
        sign_in_form = twitterforms.SignInForm() 
    return render_to_response(prefix + 'login.html',
        {'sign_up_form': sign_up_form,'sign_in_form':sign_in_form},
        RequestContext(request))

@login_required(login_url='/')
def profile_page(request):
    myuser = request.user.tweeter
    if request.method == 'POST':
        tweet_form = twitterforms.TweetForm(request.POST)
        if tweet_form.is_valid():
            tweet_form.save()
            tweet_form = twitterforms.TweetForm()
    else:
        tweet_form = twitterforms.TweetForm()
    return render(request,'mainpage.html', {'tweet_form': tweet_form, 'myuser': myuser,'current_time':datetime.datetime.now()})

def logout(request):
    auth.logout(request) 
    return HttpResponseRedirect('/')

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Tweet
    serializer_class = TweetSerializer 

class TweetList(generics.ListCreateAPIView):
    model = Tweet
    serializer_class = TweetSerializer
