# from django import forms
# from budget.models import Capital_equip,Salaryy,Investigation1,Investigation2,Consumable
# from student.models import Budget
# from guide.models import *
# from student.models import *
# from director.models import *
# from budget.models import *
# from secretariat.models import *
# from project.models import *
# class BudgetForm(forms.ModelForm):
#
#     class Meta:
#         model = Budget
#         fields = '__all__'
#         labels = {
#             'Nop': "No of Patients Sanctioned for the study",
#             "Travel_allow": "Patient Travel Allowance/Compensatory allowance",
#             "No_of_visit": "Total no of visits per patient",
#             "Rs_per_visit": "Rs per visit patient",
#             " Research_fellow_id": "Research Fellow/Clinical Asst",
#             "Miscellan":"Miscellaneous"
#         }
#
#
# class CapitalForm(forms.ModelForm):
#
#     class Meta:
#         model = Capital_equip
#         fields = ("Name", "Price")
#
#
# class Invest1(forms.ModelForm):
#
#     class Meta:
#         model = Investigation1
#         fields = ("tests", "exist_test_id", "No_of_pat", "Tarrif")
#         labels = {
#             "tests" : "Name of Test",
#             "exist_test_id" : "Existing Test",
#             "No_of_pat": "No of Patients",
#         }
#
#
# class Salary(forms.ModelForm):
#
#     class Meta:
#         model = Salaryy
#         fields = ("Name", "Study", "Salary")
#
#
# class Invest2(forms.ModelForm):
#     class Meta:
#         model = Investigation2
#         fields = ("tests", "exist_test_id", "No_of_pat", "Followup", "Tarrif")
#         labels = {
#             "tests": "Name of Test",
#             "exist_test_id": "Existing Test",
#             "No_of_pat": "No of Patients",
#             "Followup" : "Follow-up"
#         }
#
#
# class Consumable(forms.ModelForm):
#     class Meta:
#         model = Consumable
#         fields = ("consum_name", "qty", "Rs_per_unit", "Catlog_no", "Name_of_manufact")
#         labels ={
#             "consum_name" : "Consumables Name",
#             "qty" : "Quantity Required",
#             "Rs_per_unit" : "Rate/Unit",
#             "Catlog_no" : "Catalog Number",
#             "Name_of_manufact" : "Name of Manufacturer / Supplier"
#         }


        ####SHUBHAM FORMS


#
# class princi_form(forms.ModelForm):
#     class Meta:
#         model = Principal_investigator
#         fields = ['P_designation','P_Dept']
#         labels ={
#             'P_designation':'Designation',
#             'P_Dept':'Department',
#         }
#
#
# class coinv_form(forms.ModelForm):
#     class Meta:
#         model = Co_Investigator
#         fields = ['Co_designation']
#         labels = {'Co_designation': 'Designation'}

#
# class research_fellow_form(forms.ModelForm):
#     class Meta:
#         model = Std_details
#         fields = [ 'st_designation']
#         labels = {'st_designation': 'Designation',}
#
# class student_details_form(forms.ModelForm):
#     class Meta:
#         model = Std_details
#         fields = ['st_study_purpose', 'st_study_other','st_any_pub']
#         labels = {'st_study_purpose':'Select Study Purpose','st_study_other':'Others (Specify)',
#                   'st_any_pub':'Any Publications or work in the field of the Study,(not necessarily restricted to the present study) by investigator'}
#
# class project_form(forms.ModelForm):
#     class Meta:
#         model = project_details
#         fields = ['enroll_period','period_of_data','budget_estimate','choose_fund','sample_size','conflict_of_interest','conflict_comment']
#         labels = {'enroll_period':'Enrollment period for prospective study',
#                   'period_of_data':'Period of Data to be included in the retrospective study',
#                   'budget_estimate':'Budget Estimate(Total Amount)',
#                   'choose_fund':'Select Funding Body','sample_size':'Sample Size','conflict_of_interest':'Conflict of Interest to conduct the study','conflict_comment':'If Yes Provide Details'}
#
# class time_frame_form(forms.ModelForm):
#     class Meta:
#         model = Time_Frame
#         fields = ['study_coll_period','retro_period','patient_part','data_analysis','Thesis_submis']
#         labels = {'study_coll_period':'Prospective studies Enrolment sample collection period',
#                   'retro_period':'Retrospective studies-Data acquisition',
#                   'patient_part':'Period of individual patient participation not of the whole study for prospective study',
#                   'data_analysis':'Data Analysis',
#                   'Thesis_submis':'Write up & submission of Synopsis/Thesis/Paper'}
#
#
# class collab_form(forms.ModelForm):
#     class Meta:
#         model = collaborations
#         fields= ['Institue','Name','Designation','Ec_approval','Collab_type','Authorship']
#         labels = {'Institue':'Institution / agency name',
#                   'Name':'Name of Collaborator',
#                   'Designation':'Designation of Collaborator',
#                   'Ec_approval':'EC approval of Collaborators Institution',
#                   'Collab_type':'Type of collaboration, provide details(what will be done at the collaborating center) (attach additional paper if necessary)',
#                   'Authorship':'Authorship of publication(s) based of the study'}

# class show_date(forms.ModelForm):
#     class Meta:
#         model = test
#         fields = ['text1','dat']
#
# class study_design_form(forms.ModelForm):
#     class Meta:
#         model = study_design
#         fields = ['cs_report','cs_series','srvey','others']
#         labels = {'cs_report':'Case Report','cs_series':'Case Series','srvey':'Survey','others':'Others(Specify)'}
#
# class step_study_form(forms.ModelForm):
#     class Meta:
#         model = pat_sel_id
#         fields = ['define_pop','In_criteria','Ex_criteria']
#         labels = {'define_pop':'Define Population','In_criteria':'Inclusion Criteria','Ex_criteria':'Exclusion criteria'}
#
# class step_study_form2(forms.ModelForm):
#     class Meta:
#         model = work_up
#         fields = ['clinical','Investigations']
#         labels = {'clinical':'Clinical','Investigations':'Investigations'}
#
# class step_study_form3(forms.ModelForm):
#     class Meta:
#         model = study_step
#         fields = ['informed_consent','Intevention_code','Questionaire_valid','Regional_lang',
#                   'med_id','surgical_id','lab_id',
#                   'outcome_measure_id','methodology','proforma','translation','budget_id','outside_fund']
#         labels = {'informed_consent':'Informed Consent',
#                   'Intevention_code':'Intervention(s) Additional not as part of standard of care(Tick  applicable)',
#                   'Questionaire_valid':'Questionnaire Validated English Version',
#                   'Regional_lang':' Regional language versions -',
#                   'med_id':'Medical Studies provide link',
#                   'surgical_id':'Surgical Studies provide link',
#                   'lab_id':'Laboratory Studies',
#                   'outcome_measure_id':'c) Enumerate the outcome measures (State what will be measured \
# These are end points that would be used to analyze the data to answer the \
# objectives test the hypothesis efficacy safety measures, etc) \
# Provide details of Interpretation of outcome measures eg lab values, scales \
# questionnaires etc',
#                   'methodology':'Methodology / techniques to be employed for evaluating the results\
# (including statistical methods)\
# Consult In-house statistician if necessary for use of MS Excel Submit relevant &\
# appropriate data)\
# \
# Provide basic outline of\
# How data will be recorded?\
# How the data will be presented?\
# Statistical tests that will be applied (State what will be compared with what\
# Software that will be used for statistics\
# Level of significance',
#                   'proforma':'10 Proforma to record patient & study details (including results of\
# Investigations / interventions)\
# Attach a copy of the proforma that will be used to record all the findings Do not print\
# name of the patient. Print ID nos Title the proforma and write the names of Plant RF\
# Do not just paintings Attach proformas will be used to record the findings)',
#                   'translation':'',
#                   'budget_id':'Duly filled Budget proposal form (attached as AX 1a-V1/SOP 03/V1) to be\
# submitted if the study includes expenses or requires funding from HH',
#                   'outside_fund':'Outside fund key'}
#
# class completion_report_form(forms.ModelForm):
#     class Meta:
#         model = project_details
#         fields = ['project_title','project_code_no']
#         labels = {'project_title':'Title of the Research Project','project_code_no':'Project Code Number'}
# #
# # class completion_report_form2(forms.ModelForm):
# #     class Meta:
# #         model = Principal_investigator
# #         fields = ['P_name']
# #         labels = {'P_name':'Principal Investigator'}
#
# # class completion_report_form3(forms.ModelForm):
# #     class Meta:
# #         model = Std_details
# #         fields = ['st_name']
# #         labels = {'st_name':'Research fellow / DNB Student'}
#
# class completion_report_form4(forms.ModelForm):
#     class Meta:
#         model = project_details
#         fields = ['appr_date_erb']
#         labels = {'appr_date_erb':'IRB approval date'}
#
# class completion_report_form5(forms.ModelForm):
#     class Meta:
#         model = comp_report
#         fields = ['date_study_completion']
#         labels = {'date_study_completion':'Date of study completion'}
#
# class completion_report_form6(forms.ModelForm):
#     class Meta:
#         model = clinical_studies
#         fields = ['total_sample_sanctioned','no_patients_screened','no_failures','failures_reasons','no_patients_enrolled','no_patients_discontinued']
#         labels = {'total_sample_sanctioned':'Total no of patients/samples sanctioned',
#                   'no_patients_screened':'No. of patients screened',
#                  'no_failures':'No. of screen failures with reasons',
#                  'failures_reasons':'Reasons of Failure',
#                  'no_patients_enrolled':'No of patients enrolled',
#                  'no_patients_discontinued':'No. of patients discontinued'}
#
#
# class progress_report_form(forms.ModelForm):
#     class Meta:
#         model = project_details
#         fields = ['project_title','project_code_no']
#         labels = {'project_title':'Title of the research project','project_code_no':'Project Code Number'}
#
# # class progress_report_form2(forms.ModelForm):
# #     class Meta:
# #         model = Principal_investigator
# #         fields = ['P_name']
# #         labels = {'P_name':'Principal Investigator'}
#
# # class progress_report_form3(forms.ModelForm):
# #     class Meta:
# #         model = Std_details
# #         fields = ['st_name']
# #         labels = {'st_name':'Research fellow / DNB Student'}
#
# class progress_report_form4(forms.ModelForm):
#     class Meta:
#         model = project_details
#         fields = ['appr_date_erb']
#         labels = {'appr_date_erb':'IRB approval date'}
#
# class progress_report_form5(forms.ModelForm):
#     class Meta:
#         model = prog_report
#         fields = ['date_of_comencenment','exp_date_completion','project_rate','brief_summary']
#         labels = {'date_of_comencenment':'Date of Commencement of Study','exp_date_completion':'Expected Date of Completion of Project',
#                   'project_rate':'Is the project progress as per schedule? ','brief_summary':'Is the study Clinical Study or Laboratory Study?'}
#






