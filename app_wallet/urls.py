from django.urls import path, include
from .views import ViewWallet
from rest_framework import routers 



router_desc = routers.DefaultRouter()
router_desc.register(r'wallet', ViewWallet)

urlpatterns = [
    path('api', include(router_desc.urls)),


    
    ]