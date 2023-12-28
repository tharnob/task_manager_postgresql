from django.db import models

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    priority = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
