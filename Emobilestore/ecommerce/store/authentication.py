from rest_framework import authentication
from rest_framework import exceptions
from store.models import APIKey

class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            raise exceptions.AuthenticationFailed('No API Key provided')

        try:
            api_key_obj = APIKey.objects.get(key=api_key, is_active=True)
        except APIKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API Key')

        return (api_key_obj.user, None)