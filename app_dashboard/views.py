from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app_campañas.models import Campañas_desc, Head_campañas
from django.db.models import Sum
from django.http import JsonResponse


# Create your views here.

@login_required
def vista(request):
        gastos_campa= Campañas_desc.objects.aggregate(gastos_campa=Sum('inversion'))
        gastos_modelos = 0
        gastos_influencer = 0
        
        total = 0
        cam_activas = Head_campañas.objects.filter(activa=True).count()
        modelos = 0
      
        return render (request, 'dashboard.html', context={"gastos" : total, "cantidad_cam_act":cam_activas, "cantdida_modelos":modelos} )


@login_required
def dashboard(request):
        gastos_campa= Campañas_desc.objects.aggregate(gastos_campa=Sum('inversion'))
        gastos_modelos = 0
        gastos_influencer = 0
        
        

        total = 0
        cam_activas = Head_campañas.objects.filter(activa=True).count()
        modelos = 0
        return  JsonResponse({
               "gastos" : total, 
               "cantidad_cam_act":cam_activas, 
               "cantdida_modelos":modelos
        })

        


def vista_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('app_loggin:loggin')  # Redirige al usuario a la página de login


 