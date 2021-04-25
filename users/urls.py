# users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/guide', views.SignUpGuide.as_view(), name='signup_guide'),
    path('signup/student', views.SignUpStudent.as_view(), name='signup_student'),
    path('readme', views.readme, name='readme'),
]