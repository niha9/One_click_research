from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404

from student.models import Std_details
from users.models import CustomUser
from django.template import RequestContext



from .models import Principal_investigator, project_details
from .forms import research_fellow_form, student_details_form, project_form, \
    time_frame_form, collab_form, Edit_project_details, Edit_time_frame


def display_form1(request):
    res_form = research_fellow_form
    stu_form = student_details_form
    pro_form = project_form
    tim_form = time_frame_form

    if request.POST:
        # res_form = research_fellow_form(request.POST)
        # stu_form = student_details_form(request.POST)
        pro_form = project_form(request.POST)
        tim_form = time_frame_form(request.POST)
       # sho_form = show_date(request.POST)

        if  pro_form.is_valid() \
                and tim_form.is_valid():
            #form3 = res_form.save(commit=False)
            #form4 = stu_form.save(commit=False)
            form5 = pro_form.save(commit=False)
            form6 = tim_form.save()
            #form7 = sho_form.save(commit=False)

            form5.Time_frame_id = form6
            student = Std_details.objects.filter(
                student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
            student = student[0]
            form5.stud_id = student

            student.st_project_status += 1

            form5.save()
            student.save()

            return redirect('student:student_dashboard')
            # res_form = research_fellow_form
            # stu_form = student_details_form
            # pro_form = project_form
            # tim_form = time_frame_form

        # form7 = sho_form.save(commit=False)
        # form7.save()

    context = {
               'form3': res_form,
               'form4': stu_form,
               'form5': pro_form,
               'form6': tim_form,
               }

    return render(request, "project/submission_form1.html", context)

def edit_form1(request):
    project = project_details.objects.get(
        stud_id=Std_details.objects.get(student_id=CustomUser.objects.get(username=request.user.username)))
    time_frame = project.Time_frame_id
    pro_form = Edit_project_details(instance=project,)
    pro_form.fields['PI_id'].disabled = True
    time_form = Edit_time_frame(instance=time_frame)

    if request.POST:
        pro_form = project_form(request.POST,instance=project)
        tim_form = time_frame_form(request.POST,instance=time_frame)
        if pro_form.is_valid() and tim_form.is_valid():

            pro_form.save()
            tim_form.save()
            return redirect('student:student_dashboard')

        else:
            print('foo')
    context = {
        'form5': pro_form,
        'form6': time_form,
    }

    return render(request, "project/edit_form1.html", context)


def project_view(request,id):
    project = project_details.objects.get(pk=id)
    student = project.stud_id
    context = {
        'project':project,
        'student':student,
    }

    return render(request,'project/view.html',context=context)



def display_form2(request):
    des_form = study_design_form
    pat_form = step_pat_sel
    wor_form = step_work
    inf_form = step_informed_consent
    mid_form = project_mid_form

    if request.POST:
        des_form = study_design_form(request.POST)
        pat_form = step_pat_sel(request.POST)
        wor_form = step_work(request.POST)
        inf_form = step_informed_consent(request.POST)
        mid_form = project_mid_form(request.POST)

        if des_form.is_valid() and pat_form.is_valid() and wor_form.is_valid() and inf_form.is_valid() and mid_form.is_valid():
            form1 = des_form.save()
            form2 = pat_form.save()
            form3 = wor_form.save()
            form4 = inf_form.save(commit=False)
            form5 = mid_form.save(commit=False)

            form4.patient_sel_id = form2
            form4.work_up_id = form3
            form4.save()
            form5.st_design_id = form1
            form5.study_steps_id = form4
            # form5.save()
            student = Std_details.objects.filter(
                student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
            student = student[0]
            form5.studd_id = student

            # student.st_project_status += 1

            form5.save()
            # student.save()
            return redirect('student:student_dashboard')
    context = {
        'form5': mid_form,
        'form1': des_form,
        'form2': pat_form,
        'form3': wor_form,
        'form4': inf_form,
    }
    return render(request, "student_dashboard/student_dashboard.html", context)

