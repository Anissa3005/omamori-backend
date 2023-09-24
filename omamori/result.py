from rest_framework.response import Response
from rest_framework import status


class Errors:
    def not_found_error(message):
        return Response({message}, status=status.HTTP_404_NOT_FOUND)
