from django.urls import path

from . import views


urlpatterns = [
    path("register", views.AccountRegister.as_view(), name="register"),
    path("login", views.AccountLogin.as_view(), name="login"),
    path("logout", views.AccountLogout.as_view(), name="logout"),
]
