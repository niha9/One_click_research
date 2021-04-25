from django.shortcuts import render

from users.models import *
from student.models import *
from guide.models import *
from secretariat.models import *
from director.models import *
from .forms import BudgetForm, CapitalForm, Salary,Invest1,Invest2,Consumable

# Create your views here.

# def student_dashboard(request):
#     student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
#     # guidename = Director_details.objects.filter(principal_id__in=CustomUser.objects.filter(username=student[0].guide))
#     # print(student[0].student_id)
#     # context= {
#     #     'student': student[0],
#     #     'guide': guidename[0],
#     # }
#     return render(request,'student_dashboard/student_dashboard.html')
#
# def student_profile(request):
#     return render(request,'student_dashboard/student_profile.html')
#
# def student_budget(request):
#     return render(request,'student_dashboard/student_budget.html')
#
# def student_project_details(request):
#     return render(request,'student_dashboard/student_project_details.html')
#
# def student_completion_report(request):
#     return render(request,'student_dashboard/student_completion_report.html')




#
#
#
# def guide_dashboard(request):
#     return render(request,'guide_dashboard/guide_dashboard.html')
#
# def guide_profile(request):
#     return render(request,'guide_dashboard/guide_profile.html')
#
# def guide_student(request):
#     return render(request,'guide_dashboard/guide_student.html')
#

#
#
# def director_dashboard(request):
#     return render(request,'director_dashboard/director_dashboard.html')
#
# def director_profile(request):
#     return render(request,'director_dashboard/director_profile.html')
#
# def director_student_details(request):
#     return render(request,'director_dashboard/director_student_details.html')
#
# def director_project_details(request):
#     return render(request,'director_dashboard/director_project_details.html')
#
# def director_guide_details(request):
#     return render(request,'director_dashboard/director_guide_details.html')
#
# def director_secretariat_details(request):
#     return render(request,'director_dashboard/director_secretariat_details.html')


#
#
# def secretariat_dashboard(request):
#     return render(request,'secretariat_dashboard/sec_dashboard.html')
#
# def secretariat_profile(request):
#     return render(request,'secretariat_dashboard/sec_profile.html')
#
# def secretariat_director_review(request):
#     return render(request,'secretariat_dashboard/sec_director_review.html')
#
# def secretariat_irb_review(request):
#     return render(request,'secretariat_dashboard/sec_irb_review.html')
#
# def secretariat_final_review(request):
#     return render(request,'secretariat_dashboard/sec_final_review.html')


#
#
# def sample_create_view(request):
#     bud_form = BudgetForm()
#     cap_form = CapitalForm()
#     Sal = Salary
#     in1 = Invest1
#     in2 = Invest2
#     consum = Consumable
#
#
#     if request.POST:
#         bud_form = BudgetForm(request.POST)
#         cap_form = CapitalForm(request.POST)
#         sal_form = Salary(request.POST)
#         in1 = Invest1(request.POST)
#         in2 = Invest2(request.POST)
#         consum = Consumable(request.POST)
#
#
#
#         if bud_form.is_valid() and cap_form.is_valid() and sal_form.is_valid() and in1.is_valid() and in2.is_valid() and consum.is_valid() :
#             form1 = bud_form.save()
#             form2 = cap_form.save(commit=False)
#             form3 = sal_form.save(commit=False)
#             form4 = in1.save(commit=False)
#             form5 = in2.save(commit=False)
#             form6 = consum.save(commit=False)
#
#
#             form2.Budget_id  =  form3.Salary_id = form4.invest1_id = form5.invest2_id = form6.consum_id= form1
#             form2.save()
#             form3.save()
#             form4.save()
#             form5.save()
#             form6.save()
#             bud_form = BudgetForm()
#             cap_form = CapitalForm()
#
#
#         else:
#             print(bud_form.errors, len(bud_form.errors))
#             print(cap_form.errors, len(cap_form.errors))
#             print(sal_form.errors, len(sal_form.errors))
#             print(in1.errors, len(in1.errors))
#             print(in2.errors, len(in2.errors))
#             print(cap_form.errors, len(cap_form.errors))
#
#
#
#     context = {'form1' : bud_form,
#                'form2': cap_form,
#                'form3': Sal,
#                'form4': in1,
#                'form5': in2,
#                'form6': consum
#                }
#     return render(request, "student_dashboard/student_budget.html", context)