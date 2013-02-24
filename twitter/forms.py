from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth

import twitter.models as twitter_models

class SignInForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        username = self.data['username']
        password = self.data['password']
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password): 
                raise ValidationError("Username, password do not match") 
        except User.DoesNotExist:
            raise ValidationError("User does not exist")
        return cleaned_data

class TweetForm(forms.Form):
    text = forms.CharField(max_length=140)
    author = forms.IntegerField()

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) > 140:
            raise forms.ValidationError('Tweets have a maximum length of 140 characters')
        return text

    def clean_author(self):
        author = User.objects.get(id=self.cleaned_data['author'])
        return author
    
    def save(self):
        tweet = twitter_models.Tweet(author=self.cleaned_data['author'], text=self.cleaned_data['text'])
        tweet.save()
