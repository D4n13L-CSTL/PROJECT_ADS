from django.urls import path, include
from rest_framework import routers 
from .views import View_model_descripcion, View_model_head
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router_desc = routers.DefaultRouter()
router_desc.register(r'descrip', View_model_descripcion)
router_desc.register(r'head', View_model_head)


urlpatterns = [
    path('api', include(router_desc.urls)),


    
    ]