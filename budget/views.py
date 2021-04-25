from django.http import HttpResponse
from django.shortcuts import render, redirect

from project.models import project_details
from student.models import Std_details
from users.models import CustomUser
from .forms import *
from .forms import ExtensionForm, ResearchFellowForm, MaterialForm, OtherForm
# Create your views here.

def add_form(request):

    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    student = student[0]
    project = project_details.objects.get(stud_id=student)

    bud_form = BudgetForm()
    cap_form = CapitalForm()
    Sal = Salary
    in1 = Invest1
    in2 = Invest2
    consum = Consumable


    if request.POST:
        bud_form = BudgetForm(request.POST)
        cap_form = CapitalForm(request.POST)
        sal_form = Salary(request.POST)
        in1 = Invest1(request.POST)
        in2 = Invest2(request.POST)
        consum = Consumable(request.POST)



        if bud_form.is_valid() and cap_form.is_valid() and sal_form.is_valid() and in1.is_valid() and in2.is_valid() and consum.is_valid() :
            form1 = bud_form.save()
            form2 = cap_form.save(commit=False)
            form3 = sal_form.save(commit=False)
            form4 = in1.save(commit=False)
            form5 = in2.save(commit=False)
            form6 = consum.save(commit=False)


            form2.Budget_id  =  form3.Salary_id = form4.invest1_id = form5.invest2_id = form6.consum_id= form1
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()

            student = Std_details.objects.filter(
                student_id__in=CustomUser.objects.filter(username=str(request.user.username))
            )
            student = student[0]
            student.status_choice_id = 2
            student.save()

            bud_form = BudgetForm()
            cap_form = CapitalForm()


        else:
            print(bud_form.errors, len(bud_form.errors))
            print(cap_form.errors, len(cap_form.errors))
            print(sal_form.errors, len(sal_form.errors))
            print(in1.errors, len(in1.errors))
            print(in2.errors, len(in2.errors))
            print(cap_form.errors, len(cap_form.errors))



    context = {'form1' : bud_form,
               'form2': cap_form,
               'form3': Sal,
               'form4': in1,
               'form5': in2,
               'form6': consum,
               'project' : project,
               }
    return render(request, "student_dashboard/student_budget.html", context)

def routing_logic(request):
    student = Std_details.objects.filter(student_id__in = CustomUser.objects.filter(username = str(request.user.username)))
    student = student[0]
    if(student.status_choice_id == 1 ):
        return redirect('student:budget:addform')

    if (student.status_choice_id == 2):
        return redirect('student:budget:addform')

    if (student.status_choice_id == 3):
        return redirect('student:budget:term')



#term extension
def extension_view(request):
    ext_form = ExtensionForm
    res_fell_form = ResearchFellowForm
    mat_form = MaterialForm
    other_form = OtherForm
    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    student = student[0]
    project = project_details.objects.get(stud_id=student)
    if request.POST:
        ext_form = ExtensionForm(request.POST)
        res_fell_form = ResearchFellowForm(request.POST)
        mat_form = MaterialForm(request.POST)
        other_form = OtherForm(request.POST)

        if ext_form.is_valid() and res_fell_form.is_valid() and mat_form.is_valid() and other_form.is_valid():
            be1 = ext_form.save(commit=False)
            be2 = res_fell_form.save(commit=False)
            be3 = mat_form.save(commit=False)
            be4 = other_form.save(commit=False)

            be1.save()
            be2.save()
            be3.save()
            be4.save()
            return redirect('student:student_dashboard')
    context = {'form1': ext_form,
               'form2': res_fell_form,
               'form3': mat_form,
               'form4': other_form,
               'project':project,
               }
    return render(request, "student_dashboard/student_extension.html", context)



