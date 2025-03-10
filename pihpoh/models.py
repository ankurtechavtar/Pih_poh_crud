
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class DanceLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

class Interest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

