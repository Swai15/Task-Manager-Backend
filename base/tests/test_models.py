from django.test import TestCase
from base.models import Project, Task
from datetime import date
from users.models import CustomUser

# MODEL TESTS
class ProjectModelTest(TestCase):

  def test_project_creation(self):
    user = CustomUser.objects.create(username='testuser', password='testpassword')
    project = Project.objects.create(title="test project", owner=user)
    self.assertEqual(project.title, 'test project')
    self.assertEqual(project.owner, user)
    self.assertEqual(str(project), 'test project')

class TaskModelTest(TestCase):

  def setUp(self):
    user = CustomUser.objects.create(username='testuser', password='testpassword')
    project = Project.objects.create(title="test project")
    Task.objects.create(
      title= "test task",
      description= "test description",
      due_date=date(2024, 1, 10),
      priority="Medium",
      project=project,
      owner=user,
      completed=False
    )

  def test_task_creation(self):
    task = Task.objects.get(title="test task")
    self.assertEqual(task.description, "test description")
    self.assertEqual(task.due_date, date(2024, 1, 10))
    self.assertEqual(task.priority, "Medium")
    self.assertEqual(task.project.title, 'test project')
    self.assertEqual(task.owner.username, 'testuser')
    self.assertEqual(str(task), "test task")
    self.assertEqual(task.completed, False)
