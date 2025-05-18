import requests
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import os
from urllib.parse import urlparse

CLERK_API_KEY = os.getenv("CLERK_API_KEY")






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
        
        # Opcional: puedes mapear este usuario a tu modelo interno si tienes usuarios
        user = AnonymousUser()
        return (user, token)
