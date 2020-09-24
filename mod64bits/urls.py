from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.produto import urls as produto_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('produto/', include(produto_url)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
