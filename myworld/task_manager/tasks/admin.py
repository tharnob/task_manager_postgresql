from django.contrib import admin
from .models import Task

# Register your models here.


class TaskDetails(admin.ModelAdmin):
  list_display = ("title", "description", "due_date", "priority", "created_at",)

admin.site.register(Task, TaskDetails)