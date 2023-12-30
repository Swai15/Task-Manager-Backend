from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=50)

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

  def __str__(self):
    return self.title