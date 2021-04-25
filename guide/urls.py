from django.urls import path
from . import views
app_name = 'guide'

urlpatterns = [
    path('guide/home/', views.guide_dashboard, name='guide_dashboard'),
    path('guide/profile/', views.guide_profile, name='guide_profile'),
    path('guide/student/', views.guide_student, name='guide_student'),
    path('guide/initreview/<int:pk>', views.initreview,name='initreview'),
    path('guide/interreview/<int:pk>', views.interreview, name='interreview'),
    path('guide/finalreview/<int:pk>', views.finalreview, name='finalreview'),
    path('guide/initmodify/<int:pk>', views.initmodifychanges, name='initmodify'),
    path('guide/intermodify/<int:pk>', views.intermodifychanges, name='intermodify'),

]
