from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth

import twitter.models as twitter_models

class SignInForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self,request=None):
        if request:
            super(SignInForm,self).__init__(request.POST)
            self.request = request
        else:
            super(SignInForm,self).__init__()

    def clean(self):
        super(SignInForm,self).clean()
        username = self.data['username']
        password = self.data['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError("User does not exist")
        #self.user = auth.authenticate(username = username, password = password
        if not user.check_password(password): 
            raise ValidationError("Username, password do not match") 

class TweetForm(forms.Form):
    text = forms.CharField(max_length=140)

    def __init__(self,request = None):
        if request: 
            super(TweetForm,self).__init__(request.POST)
            self.author = request.user
        else:
            super(TweetForm,self).__init__()
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) > 140:
            raise forms.ValidationError('Tweets have a maximum length of 140 characters')
        return text

    def save(self):
        tweet = twitter_models.Tweet(author=self.author, text=self.cleaned_data['text'])
        tweet.save()
