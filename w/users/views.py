from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationFrom


class SignUp(generic.CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.
