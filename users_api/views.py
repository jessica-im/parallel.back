from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer, UserAccountSerializer, ProjectSerializer
from .models import Profile, UserAccount, Project

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        username = jsonRequest['username'] #get the email from the request
        password = jsonRequest['password'] #get the password from the request
        if UserAccount.objects.get(username=username): #see if email exists in db
            user = UserAccount.objects.get(username=username)  #find user object with matching email
            if check_password(password, user.password): #check if passwords match
                return JsonResponse({'id': user.id, 'username': user.username}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                return JsonResponse({})
        else: #if email doesn't exist in db, return empty dict
            return JsonResponse({})
