from django.urls import path
from . import views
app_name = 'irb'

urlpatterns = [
   path('home/', views.irb_dashboard, name='irb_dashboard'),
   path('approvals/',views.irb_approvals, name ='irb_approvals'),
   path('minutes',views.irb_minutes, name = 'irb_minutes_of_meeting'),
   path('irb_approve/<int:pk>', views.irb_approve, name='irb_approved'),
   path('irb_modified/<int:pk>', views.irb_modified, name='irb_modified'),

]