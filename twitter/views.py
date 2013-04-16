from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect
MOBILE_ROOT = 'mobile/'
import logging
from twitter.common_view_lib import login_view
import twitter.forms as twitterforms
from django.shortcuts import render

def landing_page(request):
    logging.error('got me')
    if request.user.is_authenticated():
        return profile_page(request)
    else:
        return login_view(request,'', 'login.html')

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
    return render(request,'mainpage.html', {'tweet_form': tweet_form, 'myuser': myuser})

def logout(request):
    auth.logout(request) 
    return HttpResponseRedirect('/')
