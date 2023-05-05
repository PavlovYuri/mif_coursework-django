from django import forms
from django.forms import ModelForm
from .models import UserProfile, AnalyticalPlan
from django.contrib.auth.models import User

class UserForm(ModelForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number']

