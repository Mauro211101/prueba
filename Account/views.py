from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin  
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index")


class Login(LoginView):
    next_page = reverse_lazy("post-list")

class Logout(LogoutView):
    template_name = "registration/logout.html"


