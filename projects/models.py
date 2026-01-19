from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class projectStatus(models.IntegerChoices):
    PENDING = 1 , 'pending'
    COMPLETED = 2 , 'completed'
    POSTPONED = 3 , 'postponed'
    CANCELED = 4 , 'canceled'

class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class project(models.Model):
    title = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=projectStatus.choices, default=projectStatus.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
