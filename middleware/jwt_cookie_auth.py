from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        print("🟢 CustomJWTAuthentication activa")
        access_token = request.COOKIES.get('access_token')
        print(f"🔍 Token recibido: {access_token}")
        if access_token is None:
            print("❌ Token no encontrado en cookie")
            return None
        try:
            validated_token = self.get_validated_token(access_token)
            print(f"✅ Token válido: {validated_token}")
            user = self.get_user(validated_token)
            return (user, validated_token)
        except Exception as e:
            print(f"❌ Token inválido: {e}")
            return None



