from distutils.log import Log
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class BlogList(ListView):
    template_name = "blog/blog_list.html"
    queryset = models.BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = "blogs"


class BlogDetail(DetailView):
    template_name = "blog/blog_detail.html"
    model = models.BlogPost
    context_object_name = "blog"


class BlogWriteView(LoginRequiredMixin, CreateView):
    template_name = "blog/blog_write.html"
    model = models.BlogPost
    form_class = forms.BlogCreationForm
    success_url = reverse_lazy("page:home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "blog/blog_update.html"
    model = models.BlogPost
    form_class = forms.BlogUpdationForm
    success_url = reverse_lazy("page:dashboard")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.slug = ''
        self.object.save()
        return super().form_valid(form)
