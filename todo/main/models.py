from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250, blank=False)
    active = models.BooleanField(default=True)
