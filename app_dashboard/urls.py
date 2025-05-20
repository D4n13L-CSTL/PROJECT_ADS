from django.urls import path, include
from .views import dashboard



urlpatterns = [
    path('api/dashboard', dashboard, name='api'),

    ]