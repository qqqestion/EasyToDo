from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256, default='ToDo')
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
