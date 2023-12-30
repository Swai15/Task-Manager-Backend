from rest_framework import serializers
from .models import Task, Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title',)

  def create(self, validated_data):
    user = self.context['request'].user
    validated_data['owner'] = user
    return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

  def create(self, validated_data):
    user = self.context['request'].user
    validated_data['owner'] = user
    return super().create(validated_data)


