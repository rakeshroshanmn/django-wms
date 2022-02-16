from django.db import models

# Create your models here.

class user_data(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)