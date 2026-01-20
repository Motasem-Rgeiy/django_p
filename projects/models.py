from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class projectStatus(models.IntegerChoices):
    PENDING = 1 , _('pending')
    COMPLETED = 2 , _('completed')
    POSTPONED = 3 , _('postponed')
    CANCELED = 4 , _('canceled')

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
    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
