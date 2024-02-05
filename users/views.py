from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer


@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
