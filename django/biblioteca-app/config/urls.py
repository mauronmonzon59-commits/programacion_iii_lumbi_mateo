from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('admin/', admin.site.urls),
    path('inicio/', include('catalogo.url.home_urls')),
    path('catalogo/', include('catalogo.url.categoria_urls')),
    path('catalogo/', include('catalogo.url.libro_urls')),
    path('catalogo/', include('catalogo.url.autor_urls')),
    path('cuentas/', include('catalogo.url.authentication_url')),
]
