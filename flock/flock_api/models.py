from uuid import uuid4
from django.db import models


class Task(models.Model):
    id = models.CharField(max_length=256, default=uuid4(), primary_key=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)