from django.urls import path
from . import views
app_name = 'secretariat'

urlpatterns =[
    path('secretariat/home/', views.secretariat_dashboard, name='secretariat_dashboard'),
    path('secretariat/profile/', views.secretariat_profile, name='secretariat_profile'),
    path('secretariat/director_review/', views.secretariat_director_review, name='secretariat_director_review'),
    path('secretariat/irb_review/', views.secretariat_irb_review, name='secretariat_irb_review'),
    path('secretariat/final_review/', views.secretariat_final_review, name='secretariat_final_review'),
    path('secretariat/updatedr/<int:pk>',views.upstatdr,name='update_statusdr'),
    path('secretariat/updateirb/<int:pk>', views.upstatdr, name='update_statusirbr'),
    path('secretariat/updatefinr/<int:pk>', views.upstatdr, name='update_statusdfinr'),
    path('secretariat/email/<int:pk>',views.email,name='send_email')
]

