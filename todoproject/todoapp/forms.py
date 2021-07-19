from todoapp.models import Task
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        exclude=['user']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
