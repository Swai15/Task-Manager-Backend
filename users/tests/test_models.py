from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser

# Create your tests here.

class CustomUserModelTest(TestCase):
  def test_user_creation(self):
    user = CustomUser.objects.create(
      username="testuser",
      first_name="test",
      last_name="user",
      email="test@email.com",
    )

    self.assertEqual(user.username, "testuser")
    self.assertEqual(user.first_name, "test")
    self.assertEqual(user.last_name, "user")
    self.assertEqual(user.email, "test@email.com")

