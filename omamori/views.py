from django.http import JsonResponse
from .models import Users, Omamori
from .serializers import UsersSerializer, OmamoriSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def users_list(request):

    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.errors
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_by_id(request, id):

    try:
        users = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.errors
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def omamori_by_userid(request, id):

    try:
        omamori = Omamori.objects.get(users_id=id)
        serializer = OmamoriSerializer(omamori)
        return Response(serializer.data)
    except Omamori.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)
