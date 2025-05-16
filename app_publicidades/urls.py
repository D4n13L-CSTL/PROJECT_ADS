from django.urls import path, include
from .views import  HeaderViewSet, DescripcionesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'crear', HeaderViewSet)
router.register(r'items', DescripcionesViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
]
