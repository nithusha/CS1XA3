from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInfo

class UpdateUserInfoForm(UserChangeForm):

    employment = forms.CharField(required=False)
    location = forms.CharField(required=False)
    birthday = forms.DateField(label = "Birthday MM/DD/YYYY", required=False)
    password = None
    class Meta:
        model = UserInfo
        fields = ['employment', 'location', 'birthday']

class InterestForms(UserChangeForm):
    password = None
    interests = forms.CharField(label = "Interests", required=False)
    class Meta:
        model = UserInfo
        fields = ['interests']
