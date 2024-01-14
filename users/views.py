from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

class UserRegisterView(generics.CreateAPIView):
  serializer_class = CustomUserSerializer
  permission_classes = [AllowAny]

  # def create(self, request, *args, **kwargs):
  #   serializer = self.get_serializer(data=request.data)
  #   serializer.is_valid(raise_exception=True) 

  #   password = request.data.get('password')
  #   confirm_password = request.data.get('confirm_password')

  #   if password != confirm_password:
  #     return Response({'Error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
    
  #   user = serializer.save()
  #   user.set_password(password)
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    # JWT generate:
    refresh = RefreshToken.for_user(user)
    tokens = {'refresh': str(refresh), 'access': str(refresh.access_token)}

    headers = self.get_success_headers(serializer.data)
    return Response({'user': serializer.data, 'tokens': tokens}, status=status.HTTP_201_CREATED, headers=headers)

