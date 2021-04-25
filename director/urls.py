from django.urls import path
from . import views
app_name = 'director'

urlpatterns = [
    path('director/home/', views.director_dashboard, name='director_dashboard'),
    path('director/profile/', views.director_profile, name='director_profile'),
    path('director/student_details/', views.director_student_details, name='director_student_details'),
    path('director/project_details/', views.director_project_details, name='director_project_details'),
    path('director/guide_details/', views.director_guide_details, name='director_guide_details'),
    path('director/secretariat_details/', views.director_secretariat_details, name='director_secretariat_details'),
    path('director/project_approval/', views.project_approval, name='project_approval'),
    path('director/approved/<pk>', views.project_approved, name='director_approve'),
    path('director/modfied/<pk>', views.project_modified, name='director_modify'),

]
