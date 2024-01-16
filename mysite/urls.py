from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pages.urls', 'page'), namespace='page')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('', include(('account.urls', 'account'), namespace='account')),

    path('', RedirectView.as_view(url='/home', permanent=False)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)