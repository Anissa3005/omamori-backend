from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import Users
from .serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .result import Errors
# from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET', 'POST'])
def users_list(request):

    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        print("POST request", request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Errors.bad_request('Could not create a user, make sure your inputs are')
        else:
            print('SERIALIZER_ERROR', serializer.errors)
            print('SERIALIZER', serializer)
            print('REQUEST', request.data)
            return Errors.bad_request('Could not create a user, make sure your inputs are')


@api_view(['GET'])
def user_by_uuid(request, uuid):
    try:
        users = Users.objects.get(pk=uuid)
    except Exception as error:
        print('ERROR:', error)
        print('uuid:', uuid)
        return Errors.not_found_error('This user does not exist.')

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)
