from django.urls import path
from . import views
app_name = 'guide'

urlpatterns = [
    path('co_inv/home/', views.co_inv_dashboard, name='co_inv_dashboard'),
    path('co_inv/profile/', views.co_inv_profile, name='co_inv_profile'),
    path('co_inv/student/', views.co_inv_student, name='co_inv_student'),
]
