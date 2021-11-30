from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/profile', views.ProfileList.as_view(), name='profile_list'),
    path('api/profile/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    path('api/project', views.ProjectList.as_view(), name='project_list'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login"),
    path('api/project/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
]
