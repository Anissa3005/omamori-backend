import jwt
import os

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from dotenv import load_dotenv
from rest_framework import permissions

load_dotenv()


class VerifyUser(permissions.BasePermission):

    def has_permission(self, request, view):
        print("Verifing user 🔎")
        token = request.COOKIES.get('jwt')

        secret_key = os.environ["SECRET_KEY"]
        algorithm = os.environ["ALGORITHM"]

        if not token:
            raise AuthenticationFailed(
                'Not authenticated', status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(
                'Not authenticated', status.HTTP_401_UNAUTHORIZED)

        return payload is not None
