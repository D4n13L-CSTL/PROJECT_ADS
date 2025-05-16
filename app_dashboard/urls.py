from django.urls import path, include
from .views import vista, vista_logout,dashboard



urlpatterns = [
    path('', vista, name='dashboard'),
    path('api/dashboard', dashboard, name='api'),
    path('logout/', vista_logout, name='logout'),

    ]