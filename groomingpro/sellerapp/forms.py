from .models import *
from django import forms
from django.contrib.auth.models import User

class regform(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    cpassword=forms.CharField(label='cpassword',widget=forms.PasswordInput)
    email=forms.EmailField(label='email')
    phone=forms.IntegerField(label='phone')
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone','password','cpassword']