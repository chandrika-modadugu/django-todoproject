from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title=models.CharField(max_length=200)
    Notes=models.CharField(max_length=200,default='')
    completed=models.BooleanField(default=False)
    update_date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.Title
