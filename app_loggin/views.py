from django.shortcuts import render, redirect
import bcrypt
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.permissions import AllowAny


# Create your views here.
class Template:
    def vista_loggin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username and password:
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)

                    # Generar los tokens JWT
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    refresh_token = str(refresh)

                    print(access_token)

                    # Crear la respuesta y guardar los tokens en cookies HTTPOnly
                    response = redirect(reverse('dashboard'))
                    response.set_cookie('access_token', access_token, httponly=True, secure=True, samesite='Lax')
                    response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True, samesite='Lax')

                    return response

        
        
    

class RefreshTokenFromCookieView(APIView):
    permission_classes = [AllowAny]  # ESTO ES CLAVE
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({'detail': 'No refresh token'}, status=401)

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
        except InvalidToken:
            return Response({'detail': 'Invalid refresh token'}, status=401)

        # Devuelve el nuevo access_token como cookie
        response = Response({'detail': 'Access token renewed'})
        response.set_cookie('access_token', access_token, httponly=True, secure=False, samesite='Lax')
        return response