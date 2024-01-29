from django.db import models
from users.models import CustomUser

class Project(models.Model):
  ICON_CHOICES = [
    ('default', 'Default'),
    ('home', 'Home'),
    ('work', 'work'),
    ('health', 'Health'),
    ('savings', 'Savings'),
    ('social', 'Social'),

  ]

  title = models.CharField(max_length=50)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
  tasks = models.ManyToManyField('base.Task', related_name='project_tasks')
  icon = models.CharField(max_length=10,
  choices = ICON_CHOICES, default='default')
  created_at =  models.DateTimeField(auto_now_add=True)

  def __str__ (self):
    return self.title

  class Meta: 
    ordering = ['created_at']

class Task(models.Model):
  CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
  ] 
  title = models.CharField(max_length=50, blank=False, null=False)
  description = models.TextField(blank=True)
  due_date = models.DateField()
  priority = models.CharField(max_length=10 ,choices=CHOICES)
  project = models.ForeignKey('base.Project', on_delete=models.CASCADE, related_name='tasks_project')
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title


