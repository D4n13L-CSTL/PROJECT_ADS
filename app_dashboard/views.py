from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app_campañas.models import Campañas_desc, Head_campañas
from app_perfiles.models import Header_Modelos
from app_pautasMaker.models import Pautas
from django.db.models import Sum
from django.http import JsonResponse


# Create your views here.



def dashboard(request):
        gastos_campa= Campañas_desc.objects.aggregate(gastos_campa=Sum('inversion'))
        gastos_modelos = 0
        gastos_influencer = 0
        
        
        

        total = 0
        cam_activas = Head_campañas.objects.filter(activa=True).count()
        
        modelos = Header_Modelos.objects.values().count()
        
        gastos_campa= Campañas_desc.objects.aggregate(gastos_campa=Sum('inversion'))
        gastos_pautas = Pautas.objects.aggregate(pautas=Sum('monto_de_pauta'))
        total = [(campana, pautas) for campana,pautas in zip(gastos_campa.values(), gastos_pautas.values())] 
        
        pagos_realizados = Pautas.objects.filter(autorizacio_comercial = True, autorizacion_directiva = True, status_pauta = 'PROCESADA').values().count()
        
        total_cantidad_pagos_modelos = Pautas.objects.filter(autorizacio_comercial = True, autorizacion_directiva = True,status_pauta = 'PROCESADA').aggregate(total=Sum('monto_de_pauta'))['total']
        
        total_cantidad_pagos_pendientes = Pautas.objects.filter(autorizacio_comercial = True, autorizacion_directiva = True,status_pauta = 'ACTIVA').values().count()
       
       
        modelos_prueba = Pautas.objects.select_related('modelo').all()
        
  
        
        return  JsonResponse({
               "gastos_total" : sum(total[0]), 
               "cantidad_campanas_act":cam_activas, 
               "cantdida_modelos":modelos,
               "pagos_completado":pagos_realizados,
               "pagos_totales_modelos":total_cantidad_pagos_modelos,
               "pagos_pendietnes":total_cantidad_pagos_pendientes,
               "datos_modelos":[{"nombre_modelo":i.modelo.nombres,
                                 "foto_perfil":i.nombre_pauta,
                                 "monto_pauta":i.monto_de_pauta,
                                 "estado_pauta":i.status_pauta,
                                 "foto_perfil":request.build_absolute_uri(i.modelo.foto_perfil.url) if i.modelo.foto_perfil else None,
                                 }for i in modelos_prueba]
               
               
               
               
               
        })

        


 