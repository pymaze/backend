import jwt

from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        This method called on every request regardless of whether
        the endpoint requires authentication.

        Two possible return cases:

        1) 'None' - Do not wish to authenticate/know it will fail.

        2) '(user, token)' - We return a user/token combo when authentication
        is successful. If neither case is met, there's an error and don't return anything.
        Instead raise an exception and let DRF handle it.
        """

        request.user = None

        # 'auth_header' should be an array with two elements:
        # 1) name of header ('Token')
        # 2) the JWT itself
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            # Invalid, no credentials provided. Don't attempt to authenticate
            return None
        elif len(auth_header) > 2:
            # Invalid, Token string should not contain spaces. Don't authenticate.
            return None

        # decode prefix and token
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            # Auth header not what we expected. Don't authenticate.
            return None
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw and error.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = "Invalid authentication. Could not decode token."
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = "No user matching this token was found."
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "This user has been deactivated."
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
