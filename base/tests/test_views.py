from django.test import TestCase
from base.models import Project, Task
from datetime import date
from users.models import CustomUser

from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse


# VIEW TESTS

class ProjectViewsTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = get_user_model().objects.create_user(username='testuser', password='password')
    self.client.force_authenticate(user=self.user)
    self.project_data = {'title': 'test project'}

  def test_project_list_create_view(self):
    response = self.client.post('/api/projects/', data=self.project_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Project.objects.count(), 1)

  def test_project_detail_view(self):
    project = Project.objects.create(title='test project', owner=self.user)
    url = reverse('project-detail', kwargs={'pk': project.id}) 
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], 'test project')


class TaskViewTests(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
    self.client.force_authenticate(user=self.user)
    self.project = Project.objects.create(title='test project', owner=self.user)
    self.task_data = {
      'title': 'test task',
      'description': 'test description',
      'due_date': date(2024,1,10),
      'priority': 'Medium',
      'project': self.project.id,
    }

  def test_task_list_create_view(self):
    response = self.client.post('/api/tasks/', data=self.task_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Task.objects.count(), 1)

  def test_task_detail_view(self):
    self.task_data = {
      'title': 'test task',
      'description': 'test description',
      'due_date': date(2024,1,10),
      'priority': 'Medium',
      'project': self.project,
    }
    task = Task.objects.create(**self.task_data, owner=self.user)
    url = reverse('task-detail', kwargs={'pk': task.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], 'test task')
  
