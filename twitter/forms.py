from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth
import ipdb

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
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError("User does not exist")
        self.user = auth.authenticate(username = username, password = password)
        if not self.user: 
            raise ValidationError("Username, password do not match") 

    def save(self):
        auth.login(self.request, self.user)
        return self.user
