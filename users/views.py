from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


from users.serializers import UserSerializer
from users.premissions import VerifyUser
from users.models import User
from .auth import create_token


@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username=username).first()

    if user is None:
        raise AuthenticationFailed('Username is incorect')

    if not user.check_password(password):
        raise AuthenticationFailed('Password is incorect')

    token = create_token(user=user)

    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {
        'jwt': token
    }

    return response


# Used as testing authentication using premissions
# @api_view(['GET'])
# @permission_classes([VerifyUser])
# def id_user(request):
#     return Response('Authenticated', status=status.HTTP_200_OK)
