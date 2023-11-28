from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from enum import Enum


class Error(Enum):
    INVALID_CHARACTERS = 'SINVALID_CHARACTERS'
    CONTAINS_NON_LATIN_CHARACTERS = 'CONTAINS_NON_LATIN_CHARACTERS'
    INVALID_LENGTH = 'INVALID_LENGTH'


class Errors:
    def not_found_error(message):
        return Response({message}, status=status.HTTP_404_NOT_FOUND)

    def bad_request(message):
        return Response({message}, status=status.HTTP_400_BAD_REQUEST)
