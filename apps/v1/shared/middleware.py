from django.utils import translation
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from icecream import ic

class UserLanguageMiddleware:
    """
    DRF-style middleware that runs *after* JWT authentication.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        # Try authenticating via JWT
        try:
            auth = self.jwt_auth.authenticate(request)
            if auth:
                request.user, _ = auth
        except AuthenticationFailed:
            pass

        # Now activate language if user exists
        lang_code = None
        # ic(request.user.is_authenticated)
        if request.user and request.user.is_authenticated:
            profile = getattr(request.user, "profile", None)
            # ic(profile)
            if profile and profile.app_language:
                lang_code = getattr(profile.app_language, "code", None)

        if lang_code:
            # ic(lang_code)
            translation.activate(lang_code)
            request.LANGUAGE_CODE = lang_code
            # ic(request.LANGUAGE_CODE)

        response = self.get_response(request)
        translation.deactivate()
        # ic(response)
        return response
