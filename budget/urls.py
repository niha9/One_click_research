from django.urls import path

from budget import views

app_name = 'budget'

urlpatterns = [
    path('add_form/', views.add_form, name='addform'),
    # todo add_forms budget must be linked to student

    path('term/', views.extension_view, name='term'),
    path('', views.routing_logic, name='route'),
]
