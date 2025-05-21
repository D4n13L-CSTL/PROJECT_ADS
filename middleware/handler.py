from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework.exceptions import AuthenticationFailed



def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 401:
            # Si el error es AuthenticationFailed y el mensaje contiene "expirado"
            if isinstance(exc, AuthenticationFailed) and "expirado" in str(exc).lower():
                response.data = {
                    "error": "Token expirado. Por favor, renuevac la sesión."
                }
            else:
                response.data = {
                    "error": "Autenticación requerida. Por favor, envía el token."
                }
        elif response.status_code == 403:
            response.data = {
                "error": "No tienes permiso para acceder a este recurso."
            }

    return response



def custom_page_not_found_view(request, exception):
    
    return HttpResponse("Ruta no encontrada", status=404)
