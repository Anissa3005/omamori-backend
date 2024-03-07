from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from users import premissions

from .models import Omamori
from .serializers import OmamoriSerializer
from users.premissions import VerifyUser
# from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def index(request):
    return Response({"index"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([VerifyUser])
def omamori_list(request):

    if request.method == 'GET':
        omamori = Omamori.objects.all()
        serializer = OmamoriSerializer(omamori, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = OmamoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # TO DO: Should only return id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('SERIALIZER_ERROR', serializer.errors)
            print('SERIALIZER', serializer)
            print('REQUEST', request.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
