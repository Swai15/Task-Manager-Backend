from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserRegisterTest(APITestCase):
  def test_user_registration(self):
    url = reverse('user-register')
    data = {
      'username': 'testuser',
      'password': 'testpassword',
      'confirm_password': 'testpassword',
      'first_name': 'test',
      'last_name': 'user',
      'email': 'test@email.com'
      }

    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertIn('user', response.data)
    self.assertIn('tokens', response.data)
    # nested 'username' in serializer.data
    self.assertEqual(response.data['user']['username'], 'testuser')

  def test_user_registration_password_mismatch(self):
    url = reverse('user-register')
    data = {
      'username': 'testuser',
      'password': 'testpassword',
      'confirm_password': 'wrongpassword',
      'first_name': 'test',
      'last_name': 'user',
      'email': 'test@email.com'
      }

    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertIn('Passwords do not match.', str(response.data))
