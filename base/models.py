from django.db import models
from users.models import CustomUser

class Project(models.Model):
  title = models.CharField(max_length=50)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

  def __str__ (self):
    return self.title


class Task(models.Model):
  CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
  ]
  title = models.CharField(max_length=50)
  description = models.TextField()
  due_date = models.DateField()
  priority = models.CharField(max_length=10 ,choices=CHOICES)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

  def __str__(self):
    return self.title