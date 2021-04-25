from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(study_design)
admin.site.register(Time_Frame)
admin.site.register(pat_sel_id)
admin.site.register(study_step)
admin.site.register(project_details)
admin.site.register(project_details2)
admin.site.register(Out_funding)
admin.site.register(work_up)
admin.site.register(expected_comp)
admin.site.register(clinical_studies)
admin.site.register(lab_study)

