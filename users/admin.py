from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ['id', 'username', 'first_name', 'last_name', 'email']
  readonly_fields =  ['date_joined']

admin.site.register(CustomUser, CustomUserAdmin)



# admin.site.register(CustomUser, UserAdmin)