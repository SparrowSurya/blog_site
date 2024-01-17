from django.urls import path

from .import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write', views.BlogWriteView.as_view(), name='blog_write'),
    path('<slug:slug>', views.BlogDetail.as_view(), name='blog_detail'),
]
