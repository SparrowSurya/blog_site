from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms


class Signup(CreateView):
    template_name = "account/signup.html"
    success_url = reverse_lazy("account:signin")
    form_class = forms.AccountRegisterForm


class Signin(LoginView):
    template_name = "account/signin.html"
    redirect_authenticated_user = True # redirect url is handeled in settings.py


class Signout(LogoutView):
    next_page = 'page:home'
