from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib import auth
from twitter.forms import UserCreationForm
from django.http import HttpResponseRedirect
import twitter.forms as twitterforms 

def login_view(request,profile_url,template_str):
    if request.method == 'POST':
        post_action = request.POST.get('post_action','')
        if post_action == 'sign_up':
            sign_up_form = UserCreationForm(request.POST)
            if sign_up_form.is_valid():
                sign_up_form.save()
                user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
                auth.login(request,user)
                return HttpResponseRedirect(profile_url)

        elif post_action == 'sign_in':
            sign_in_form = twitterforms.SignInForm(request.POST)
            if sign_in_form.is_valid():
                user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
                auth.login(request,user)
                return HttpResponseRedirect(profile_url) 

    #Get, and bad unsuccesful login, signup 
    if not 'sign_up_form' in locals():
        sign_up_form = UserCreationForm()
    if not 'sign_in_form' in locals():
        sign_in_form = twitterforms.SignInForm() 
    return render_to_response(template_str,
        {'sign_up_form': sign_up_form,'sign_in_form':sign_in_form},
        RequestContext(request))
