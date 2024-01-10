from rest_framework import serializers
from .models import Task, Project
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'
    read_only_fields = ['id', 'owner']

  def create(self, validated_data):
    user = self.context['request'].user

    if user.is_authenticated:      
      validated_data['owner'] = user
    else:
      default_user = CustomUser.objects.get(username='admin')
      validated_data['owner'] = default_user
      print(f"test") 

    # project_title = validated_data.get('project', None)

    # if project_title: 
    #   project = Project.objects.get(title=project_title)
    #   validated_data['project'] = project.id

    return super().create(validated_data)

class ProjectSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(source='tasks_project' ,many=True, read_only=True)

  class Meta:
    model = Project
    fields = ('id', 'title', 'tasks')
    read_only_fields = ['id']

  # def validate(self, validated_data):
  #   request = self.context.validated_data('request')
  #   if request and request.method == "PUT":
  #     title = validated_data.get('title')
  #     if not title:
  #       raise serializers.ValidationError({'title': 'Title is required for updates'})
  #   return validated_data
  

  def create(self, validated_data):
    user = self.context['request'].user

    # set default user 
    if user.is_authenticated:      
      validated_data['owner'] = user
    else:
      default_user = CustomUser.objects.get(username='admin')
      validated_data['owner'] = default_user

    return super().create(validated_data)

  # Limit tasks displayed