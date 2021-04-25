from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
from .forms import CustomStudentCreationForm, CustomUserChangeForm
# from .models import CustomUser,sec_details,Std_details,Director_details,Principal_investigator


class CustomUserAdmin(UserAdmin):
     add_form = CustomStudentCreationForm
     model = CustomUser
     list_display = ['username', 'name','contact','type']
     list_editable = ['type']

admin.site.register(CustomUser, admin_class=CustomUserAdmin)
# admin.site.register(sec_details)
# admin.site.register(Director_details)
# admin.site.register(Principal_investigator)
# admin.site.register(Std_details)
admin.site.site_header="Cateina Admin"
admin.site.site_title="Cateina Admin"

#todo director profile
#todo secretary details