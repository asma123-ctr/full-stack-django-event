from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    event_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
