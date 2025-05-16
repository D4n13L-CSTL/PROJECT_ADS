from django.urls import path, include
from rest_framework import routers 

from .views import  PruebaVies


router = routers.DefaultRouter()
router.register(r'prueba', PruebaVies)


urlpatterns = [
    path('', include(router.urls))
    ]