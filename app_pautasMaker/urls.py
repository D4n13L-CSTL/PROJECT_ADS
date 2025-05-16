from django.urls import path, include
from rest_framework import routers 
from .views import  PautasView

router = routers.DefaultRouter()
router.register(r'pautas', PautasView)

urlpatterns = [

    path('api', include(router.urls))
    ]