from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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


class BlogWriteView(CreateView):
    template_name = "blog/blog_write.html"
    model = models.BlogPost
    form_class = forms.BlogCreationForm
    success_url = reverse_lazy("page:home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)