# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging
import twitter.views 
from twitter.common_view_lib import login_view
from django.core import serializers
from models import Tweet, Tweeter
import json
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.views.generic import ListView
import twitter.forms

class ApiView(View):
    all_views = {'tweets': '/api/tweets/', 'users': '/api/users'} 

    def get(self, request):
        return HttpResponse(json.dumps(self.all_views))

class UserTweets(View):

    def get(self, request, user_id):
        tweets = User.objects.get(pk=int(user_id)).tweeter.tweets
        tweet_json_obj = [t.serialized() for t in tweets]
        tweet_json_str = json.dumps(tweet_json_obj)
        return HttpResponse(tweet_json_str)

    def post(self, request, user_id):
        '''Creates a tweet for a particular user'''
        tweeter = User.objects.get(pk=int(user_id)).tweeter
        tweet_form = twitter.forms.TweetForm(request.POST)
        if tweet_form.is_valid():
            tweet_form.save()
            return HttpResponse('',status=201)
        else:
            #Is this the correct status code?
            return HttpResponse('',status=403)

class UserList(View):

    def get(self, request):
        users = Tweeter.objects.all()
        user_json = [u.serialized() for u in users] 
        return HttpResponse(json.dumps(user_json))

class TweetViews(View):

    def get(self, request, tweet_id):
        tweet = Tweet.objects.get(pk=int(tweet_id))
        return HttpResponse(json.dumps(tweet.serialized()))

class TweetList(View):

    def get(self, request):
        tweets = Tweet.objects.all().order_by('-created')
        tweet_json = [t.serialized() for t in tweets] 
        return HttpResponse(json.dumps(tweet_json))
