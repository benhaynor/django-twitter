from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth
import twitter.models
from twitter.models import Tweeter


class SignInForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        username = self.data['username']
        password = self.data['password']         
        if not auth.authenticate(username=username,password=password):
            raise ValidationError("Username, password do not match")
        return cleaned_data

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise ValidationError("User does not exist")
        return self.cleaned_data['username']

class TweetForm(forms.Form):
    text = forms.CharField(max_length=140)
    author = forms.IntegerField()

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) > 140:
            raise forms.ValidationError('Tweets have a maximum length of 140 characters')
        return text

    def clean_author(self):
        author = User.objects.get(id=self.cleaned_data['author']).tweeter
        return author
    
    def save(self):
        tweet = twitter.models.Tweet(author=self.cleaned_data['author'], text=self.cleaned_data['text'])
        tweet.save()

class UserCreationForm(forms.Form):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': ("A user with that username already exists."),
        'password_mismatch': ("The two password fields didn't match."),
    }
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = User(username=self.cleaned_data['username'],email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            new_tweeter = Tweeter(user=user)
            new_tweeter.save()
        return user
