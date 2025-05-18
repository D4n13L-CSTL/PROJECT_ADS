"""
URL configuration for ProyectoPublicidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app_init.urls')),
    path('inicio/', include('app_dashboard.urls')),
    path('campanas/', include('app_campañas.urls')),
    path('publicidad/', include('app_publicidades.urls')),
    path('modelos/', include('app_perfiles.urls')),
    path('pautas/', include('app_pautasMaker.urls')),
    path('', include('app_loggin.urls')),
    path('wallet/',include('app_wallet.urls')),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Documentación con Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Documentación con Redoc
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "middleware.handler.custom_page_not_found_view"
