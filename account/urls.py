from django.urls import path

from . import views


urlpatterns = [
    path("login", views.AccountLogin.as_view(), name="login"),
    path("logout", views.AccountLogout.as_view(), name="logout"),
]
