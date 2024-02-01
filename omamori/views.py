from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import Omamori
from .serializers import OmamoriSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from omamori.results import Errors
# from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def index(request):
    return Response({"index"}, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def users_list(request):
#     print('REQUEST', request.data)

#     if request.method == 'GET':
#         users = Users.objects.all()
#         serializer = UsersSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('SERIALIZER_ERROR', serializer.errors)
#             return Errors.bad_request('Could not create a user, make sure your inputs are')


# @api_view(['GET'])
# def user_by_uuid(request, uuid):
#     try:
#         users = Users.objects.get(pk=uuid)
#     except Exception as error:
#         print('ERROR:', error)
#         print('uuid:', uuid)
#         return Errors.not_found_error('This user does not exist.')

#     if request.method == 'GET':
#         serializer = UsersSerializer(users)
#         return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
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
