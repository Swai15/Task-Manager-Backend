from django.shortcuts import render
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project, Task

class SharedFields(APIView):
    permission_classes = [AllowAny]

# PROJECT VIEWS
class ProjectListCreateView(SharedFields, generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# detail, update and destroy 
class ProjectDetailView( SharedFields,generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

# TASK VIEWS
class TaskListCreateView(generics.ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# detail, update and destroy
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
