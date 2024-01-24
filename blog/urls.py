from django.urls import path

from .import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/new', views.BlogWriteView.as_view(), name='blog_write'),
    path('update/<slug:slug>', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>', views.BlogDetail.as_view(), name='blog_detail'),
]
