from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class TaskModelManager(models.Manager):
    def user_tasks(self, user):
        return self.filter(user=user)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    objects = TaskModelManager()

    class Meta:
        ordering = ['completed']
