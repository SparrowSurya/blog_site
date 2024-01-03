from django.views.generic import ListView, DetailView

from . import models


class PostList(ListView):
    template_name = "blog/blog_list.html"
    queryset = models.Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(DetailView):
    template_name = "blog/blog_detail.html"
    model = models.Post
