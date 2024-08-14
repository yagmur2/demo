from django.db import models

# Create your models here.
# MAKE MIGRATIONS EVERY TIME SOMETHING CHANGES

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)