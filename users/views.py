from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserRegisterView(generics.CreateAPIView):
  serializer_class = CustomUserSerializer
  permission_classes = [AllowAny]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True) 

    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if password != confirm_password:
      return Response({'Error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = serializer.save()
    user.set_password(password)
    user.save()

    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)