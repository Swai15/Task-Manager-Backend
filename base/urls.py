from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, TaskListCreateView, TaskDetail

urlpatterns = [
  path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
  path('projects/<int:pk>', ProjectDetailView.as_view(), name='project-detail' ),
  path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
  path('tasks/<int:pk>', TaskDetail.as_view(), name='task-detail')

]