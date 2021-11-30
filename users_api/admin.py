from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)

from .models import UserAccount
admin.site.register(UserAccount)

from .models import Project
admin.site.register(Project)
