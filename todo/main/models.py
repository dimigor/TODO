from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250, blank=False)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)
