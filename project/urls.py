from django.urls import path

from project import views

app_name = 'project'

urlpatterns = [
    path('', views.display_form1,name= 'project'),
    path('edit/',views.edit_form1,name = 'edit'),
    path('project/<int:id>', views.project_view, name='view'),
    path('re', views.display_form2, name='project2'),

]
