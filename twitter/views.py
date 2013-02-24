from django.contrib.auth import decorators
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
import forms as twitterforms 
import ipdb

def landing_page(request):
    if request.user.is_authenticated():
        return profile_page(request)
    if request.method == 'POST':
        post_action = request.POST.get('post_action','')
        if post_action == 'sign_up':
            sign_up_form = UserCreationForm(request.POST)
            if sign_up_form.is_valid():
                new_user = sign_up_form.save()
                return HttpResponse('Congrats, new user!')

        elif post_action == 'sign_in':
            sign_in_form = twitterforms.SignInForm(request)
            if sign_in_form.is_valid():
                user = sign_in_form.save()
                return HttpResponse("You are signed in") 

    #Get, and bad unsuccesful login, signup 
    if not 'sign_up_form' in locals():
        sign_up_form = UserCreationForm()
    if not 'sign_in_form' in locals():
        sign_in_form = twitterforms.SignInForm() 
    return render_to_response('landing_page.html',
            {'sign_up_form': sign_up_form,'sign_in_form':sign_in_form},
            RequestContext(request))

def profile_page(request):
    return HttpResponse("Welcome %s" % request.user.username)
