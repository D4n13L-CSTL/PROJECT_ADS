from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 401:
            response.data = {
                "error": "Autenticación requerida. Por favor, envía el token."
            }
        if response.status_code == 403:
            response.data = {
                "error": "No tienes permiso para acceder a este recurso."
            }


    return response



def custom_page_not_found_view(request, exception):
    
    return HttpResponse("Ruta no encontrada", status=404)
