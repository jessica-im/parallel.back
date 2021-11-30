from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    website = models.CharField(max_length=1000)

class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, default=0, on_delete=models.CASCADE)

class Project(models.Model):
    profile = models.ForeignKey(Profile, default=0, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    about = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    github = models.CharField(max_length=1000)
