from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    role = models.CharField(max_length=200, choices=[('Admin', 'Admin'), ('Student', 'Student')])

class Book(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=200)