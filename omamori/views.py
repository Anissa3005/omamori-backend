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
def user_by_id(request, id):
    try:
        users = Users.objects.get(pk=id)
    except Exception as error:
        print('ERROR:', error)
        print('ID:', id)
        return Errors.not_found_error('This user does not exist.')

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_by_username(request, username):

    try:
        user = Users.objects.get(username=username)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_by_email(request):
    email = request.data['email']

    try:
        users_id = Users.objects.get(email=email)
        serializer = UsersSerializer(users_id)
        return Response(serializer.data)
    except Users.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'POST'])
# def omamori_list(request):

#     if request.method == 'GET':
#         omamori = Users.objects.all()
#         serializer = UsersSerializer(omamori, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         serializer.errors
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def omamori_by_userid(request, id):

#     try:
#         omamori = Omamori.objects.get(users_id=id)
#         serializer = OmamoriSerializer(omamori)
#         return Response(serializer.data)
#     except Omamori.DoesNotExist:
#         Response(status=status.HTTP_404_NOT_FOUND)
