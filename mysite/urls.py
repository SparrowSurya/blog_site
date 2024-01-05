from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pages.urls', 'pages'), namespace='page')),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)