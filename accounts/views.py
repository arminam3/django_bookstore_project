from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

from .forms import  CustomUserCreationForm

class SignUpView(CreateView):
    model = User
    template_name = '../templates/registration/signup.html'
    # fields = '__all__'
    form_class = CustomUserCreationForm

class CustomPasswordChangeView(PasswordChangeView):
    template_name = '../templates/registration/password_change_form.html'



