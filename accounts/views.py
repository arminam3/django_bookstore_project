from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import  CustomUserCreationForm

class SignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    # fields = '__all__'
    form_class = CustomUserCreationForm


