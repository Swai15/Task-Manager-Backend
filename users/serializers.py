from rest_framework import serializers
from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Adds username to token payload.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class CustomUserSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True)
  class Meta:
    model = CustomUser
    fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
    read_only_fields = ('id',)
    # extra_kwargs = {'password': {'write_only': True}}

  def validate(self, data):
    if data.get('password') != data.get('confirm_password'):
      raise serializers.ValidationError("Passwords do not match")
    return data
  
  def create(self, validated_data):
    validated_data.pop('confirm_password')
    password = validated_data.pop('password')
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()
    return user


    



