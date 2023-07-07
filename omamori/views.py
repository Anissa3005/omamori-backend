from django.http import JsonResponse
from .models import Users
from .serializers import UsersSerializer
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
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_by_id(request, id):

    try:
        users = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data)
