from django.urls import path, include
from rest_framework import routers 
from .views import HeaderModelos, TallasModelos, TipoDeCuentaView,WalletsModelView,TranaccionesModelView


router_desc = routers.DefaultRouter()
router_desc.register(r'head', HeaderModelos)
router_desc.register(r'tallas', TallasModelos)
router_desc.register(r'cuenta', TipoDeCuentaView)
router_desc.register(r'wallets', WalletsModelView)
router_desc.register(r'wallestransacciones', TranaccionesModelView)


urlpatterns = [
    path('api/', include(router_desc.urls))

    
    ]