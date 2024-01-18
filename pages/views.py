from typing import Any
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import BlogPost


class HomePage(TemplateView):
    template_name = "pages/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"
    login_url = reverse_lazy("account:signin")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs = super().get_context_data(**kwargs)
        kwargs['blogs'] = BlogPost.objects.filter(author=self.request.user)
        return kwargs
