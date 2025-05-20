from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from jwt import PyJWTError, decode
from jwt import PyJWKClient

class ClerkUser:
    def __init__(self, clerk_sub, payload):
        self.clerk_sub = clerk_sub
        self.clerk_payload = payload

    @property
    def is_authenticated(self):
        return True

class ClerkAuthentication(BaseAuthentication):
    def __init__(self):
        super().__init__()
        self.jwks_client = PyJWKClient(
            f"https://{settings.CLERK_DOMAIN}/.well-known/jwks.json",
            cache_keys=True
        )

    def authenticate(self, request):
        print("🔍 Headers recibidos:", request.headers)
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            print("❌ Falta header Authorization")
            return None

        token = auth_header.split(" ")[1]
        print(f"🧪 Token recibido: {token[:10]}...")

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)
            decoded = decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=None,
                issuer=f"https://{settings.CLERK_DOMAIN}",
                options={
                    "verify_exp": True,
                    "verify_iss": True,
                    "verify_signature": True
                }
            )

            user = ClerkUser(decoded["sub"], decoded)
            print(f"✅ Token válido para clerk_sub: {decoded['sub']}")
            return (user, token)

        except PyJWTError as e:
            print("🔥 Error al verificar token:", str(e))
            raise AuthenticationFailed(f"Token inválido: {str(e)}")
