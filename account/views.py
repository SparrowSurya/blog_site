from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms


class AccountRegister(CreateView):
    template_name = "account/register.html"
    success_url = reverse_lazy("account:login")
    form_class = forms.AccountRegisterForm


class AccountLogin(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy("blog:blog_list")
    redirect_authenticated_user = True

    def get_redirect_url(self) -> str:
        return reverse_lazy("blog:blogs_list")


class AccountLogout(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy("pages:home")