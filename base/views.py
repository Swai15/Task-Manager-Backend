from django.shortcuts import render
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project, Task

# PROJECT VIEWS
class ProjectListCreateView(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# detail, update and destroy 
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

# TASK VIEWS
class TaskListCreatView(generics.ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# detail, update and destroy
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]
