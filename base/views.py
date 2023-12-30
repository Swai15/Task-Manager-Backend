from django.shortcuts import render
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task


class ProjectListCreateView(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)