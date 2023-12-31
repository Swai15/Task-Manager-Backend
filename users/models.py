from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = models.CharField(max_length=50, unique=True, blank=False)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30, blank=True)
  email = models.EmailField(unique=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.first_name