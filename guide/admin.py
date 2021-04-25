from django.contrib import admin

# Register your models here.
from guide.models import Principal_investigator, Co_Investigator

admin.site.register(Principal_investigator)
admin.site.register(Co_Investigator)
