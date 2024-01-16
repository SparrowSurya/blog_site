from django.urls import path

from . import views


urlpatterns = [
    path("signup", views.Signup.as_view(), name="signup"),
    path("signin", views.Signin.as_view(), name="signin"),
    path("signout", views.Signout.as_view(), name="signout"),
]
