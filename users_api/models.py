from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    # profile = models.ForeignKey(Profile, default=0, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    website = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'

class Project(models.Model):
    profile = models.ForeignKey(Profile, default=0, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    about = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    github = models.CharField(max_length=1000)
