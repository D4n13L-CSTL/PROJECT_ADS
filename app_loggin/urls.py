from django.urls import path, include
from .views import Template, RefreshTokenFromCookieView


app_name = 'app_loggin'

urlpatterns = [
    
    path('api/token/refresh-cookie/', RefreshTokenFromCookieView.as_view(), name='token_refresh_cookie')
    ]