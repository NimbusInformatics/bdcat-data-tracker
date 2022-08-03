import requests

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView)
from .provider import CustomProvider
from django.conf import settings


class CustomAdapter(OAuth2Adapter):
    provider_id = CustomProvider.id

    access_token_url = settings.NIH_OAUTH_SERVER_TOKEN_URL
    profile_url = settings.NIH_OAUTH_SERVER_INFO_URL
    authorize_url = settings.NIH_OAUTH_SERVER_AUTH_URL

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)

oauth2_login = OAuth2LoginView.adapter_view(CustomAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomAdapter)