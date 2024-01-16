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
    success_url = reverse_lazy("blog:blog_list")
    redirect_authenticated_user = True

    def get_redirect_url(self) -> str:
        return reverse_lazy("blog:blog_list")


class Signout(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy("page:home")