from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=1000, blank=True)


class Project(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000, blank=True)
    about = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=1000, blank=True)
    github = models.CharField(max_length=1000, blank=True)
