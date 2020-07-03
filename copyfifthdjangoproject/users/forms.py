from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import TeacherProfile,StudentProfile

class TeacherRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    #first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    #last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
