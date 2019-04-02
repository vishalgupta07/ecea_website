# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-03-31 17:22:20
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-01 17:44:27
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterform(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User #model that will be affected is the user model
		fields = ['username','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']