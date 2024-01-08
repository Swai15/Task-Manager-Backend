from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
  list_display= ('id', 'title')
  list_display_links = ('title',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)