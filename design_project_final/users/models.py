from django.contrib.auth.models import User
from django.db import models

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)