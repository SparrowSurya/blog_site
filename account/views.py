from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy


class AccountLogin(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy("blog:blog_list")
    redirect_authenticated_user = True

    def get_redirect_url(self) -> str:
        return reverse_lazy("blog:blogs_list")

# TODO
class AccountLogout(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy("pages:home")