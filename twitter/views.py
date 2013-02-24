from django.contrib.auth import decorators
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
import twitter.forms as twitterforms 
import ipdb

def landing_page(request):
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
                return HttpResponseRedirect('/')

        elif post_action == 'sign_in':
            sign_in_form = twitterforms.SignInForm(request)
            if sign_in_form.is_valid():
                user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
                auth.login(request,user)
                return HttpResponseRedirect("/") 

    #Get, and bad unsuccesful login, signup 
    if not 'sign_up_form' in locals():
        sign_up_form = UserCreationForm()
    if not 'sign_in_form' in locals():
        sign_in_form = twitterforms.SignInForm() 
    return render_to_response('landing_page.html',
            {'sign_up_form': sign_up_form,'sign_in_form':sign_in_form},
            RequestContext(request))

def profile_page(request):
    if request.method == 'POST':
        tweet_form = twitterforms.TweetForm(request)
        if tweet_form.is_valid():
            tweet_form.save()
            tweet_form = twitterforms.TweetForm()
    else:
        tweet_form = twitterforms.TweetForm()
    return render_to_response('mainpage.html', {'tweet_form': tweet_form}, RequestContext(request))

def logout(request):
    auth.logout(request) 
    return HttpResponseRedirect('/')
