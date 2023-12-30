from django.test import TestCase
from .models import Project, Task
from datetime import date

class ProjectModelTest(TestCase):

  def test_project_creation(self):
    project = Project.objects.create(title="test project")
    self.assertEqual(project.title, 'test project')
    self.assertEqual(str(project), 'test project')

class TaskModelTest(TestCase):

  def setUp(self):
    project = Project.objects.create(title="test project")
    Task.objects.create(
      title= "test task",
      description= "test description",
      due_date=date(2024, 1, 10),
      priority="Medium",
      project=project
    )

  def test_task_creation(self):
    task = Task.objects.get(title="test task")
    self.assertEqual(task.description, "test description")
    self.assertEqual(task.due_date, date(2024, 1, 10))
    self.assertEqual(task.priority, "Medium")
    self.assertEqual(str(task), "test task")

