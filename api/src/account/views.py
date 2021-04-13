from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Account
from .serializers import RegistrationSerializer


@api_view(['POST'])
@permission_classes([])
def login_view(request):
    serializer = ObtainAuthToken.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    account = Account.objects.get(email=user.email)
    token = Token.objects.get(user=account).key
    data = {
        'token': token
    }
    return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.user.auth_token.delete()
    data = {
        'logout': 'Logged out successfully'
    }
    status_code = status.HTTP_200_OK
    return Response(status=status_code, data=data)


@api_view(['POST'])
@permission_classes([])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        if Account.objects.filter(email=serializer.data['email'].lower()).count() > 0:
            data = {'email': 'account with this email already exists.'}
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            account = serializer.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data['token'] = token
            status_code = status.HTTP_201_CREATED
    else:
        data = serializer.errors
        status_code = status.HTTP_400_BAD_REQUEST
    return Response(status=status_code, data=data)
