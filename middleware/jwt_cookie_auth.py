from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from jwt import PyJWKClient, PyJWTError
import jwt

class ClerkAuthentication(BaseAuthentication):
    def __init__(self):
        super().__init__()
        self.jwks_client = PyJWKClient(
            f"https://{settings.CLERK_DOMAIN}/.well-known/jwks.json",
            cache_keys=True
        )

    def authenticate(self, request):
        print("🔍 Headers recibidos:", request.headers)  # Debug
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            print("❌ Falta header Authorization")
            return None

        token = auth_header.split(" ")[1]
        print(f"🧪 Token recibido: {token[:10]}...")  # Muestra parte del token para no imprimirlo entero

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)
            decoded = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=None,  # Si quieres validar el audience, pon aquí el valor correcto
                issuer=f"https://{settings.CLERK_DOMAIN}",
                options={
                    "verify_exp": True,
                    "verify_iss": True,
                    "verify_signature": True
                }
            )

            # Buscar o crear el usuario según el campo 'sub' del token
            User = get_user_model()
            user, created = User.objects.get_or_create(clerk_id=decoded["sub"])

            print(f"✅ Usuario autenticado: {user} (creado: {created})")

            return (user, token)

        except PyJWTError as e:
            print("🔥 Error al verificar token:", str(e))  # Debug detallado
            raise AuthenticationFailed(f"Token inválido: {str(e)}")
