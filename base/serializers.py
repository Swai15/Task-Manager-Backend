from rest_framework import serializers
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'
    read_only_fields = ['id', 'owner']

  def create(self, validated_data):
    user = self.context['request'].user
    validated_data['owner'] = user
    return super().create(validated_data)

class ProjectSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(source='tasks_project' ,many=True, read_only=True)

  class Meta:
    model = Project
    fields = ('id', 'title', 'tasks')
    read_only_fields = ['id']

  def create(self, validated_data):
    user = self.context['request'].user
    validated_data['owner'] = user
    return super().create(validated_data)
