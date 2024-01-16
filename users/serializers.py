from rest_framework import serializers
from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

# Adds username to token payload.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
      token = super().get_token(user)
      token['username'] = user.username
      return token
      

class CustomUserSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True)
  class Meta:
    model = CustomUser
    fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
    read_only_fields = ('id',)
    # extra_kwargs = {'password': {'write_only': True}}

  def validate(self, data):
    # same password check
    if data.get('password') != data.get('confirm_password'):
      raise serializers.ValidationError("Passwords do not match")

    # Unique email
    email_exists = CustomUser.objects.filter(email=data.get('email')).exists()
    if email_exists:
      raise serializers.ValidationError("User with email already exists")

    # Unique username
    username_exists = CustomUser.objects.filter(username=data.get('username')).exists()
    if username_exists:
      raise serializers.ValidationError('User with username already exists')

    return data  

  def create(self, validated_data):
    validated_data.pop('confirm_password')
    password = validated_data.pop('password')
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()
    return user


    



