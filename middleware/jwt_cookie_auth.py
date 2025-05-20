import requests
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import os
from urllib.parse import urlparse

CLERK_API_KEY = os.getenv("CLERK_API_KEY")

from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import get_user_model

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("🔐 ClerkAuthentication activa")
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Bearer "):
            print("❌ No se encontró token de Clerk")
            return None

        token = auth_header.split(" ")[1]
        print(f"🧪 Verificando token: {token}")
        
        clerk_response = requests.post(
            "https://api.clerk.dev/v1/tokens/verify",
            headers={
                "Authorization": f"Bearer {settings.CLERK_API_KEY}",
                "Content-Type": "application/json"
            },
            json={"token": token}
        )

        if clerk_response.status_code != 200:
            print("❌ Clerk no pudo verificar el token")
            raise AuthenticationFailed("Token inválido o expirado")

        data = clerk_response.json()
        print(f"✅ Respuesta de Clerk: {data}")
        
        # Usamos los datos del token para crear un usuario temporal
        email = data.get("email_address", "unknown@clerk.dev")
        username = data.get("sub", "clerk_user")

        # Crea un usuario falso (no lo guarda en la BD)
        UserModel = get_user_model()
        user = UserModel(id=None, username=username, email=email)
        user.is_authenticated = True  # le decimos que sí está autenticado
        
        return (user, token)

