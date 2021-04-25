from django.shortcuts import render, redirect

# Create your views here.
from director.models import Director_details
from guide.models import Principal_investigator, Co_Investigator
from secretariat.models import sec_details
from project.models import project_details, Std_details
from users.models import CustomUser


def director_dashboard(request):
    return render(request,'director_dashboard/director_dashboard.html')

def director_profile(request):
    dir = Director_details.objects.filter(director_id__in=CustomUser.objects.filter(username=request.user.username))
    print(dir)
    dir = dir[0]
    context = {
        'dir': dir
    }
    return render(request,'director_dashboard/director_profile.html',context)

def director_student_details(request):
    sec = project_details.objects.all()
    # student = Std_details.objects.filter(student_id__in=project_details.objects.filter(stud_id))
    context = {
        'sec': sec,
        # 'student':student,
    }
    return render(request,'director_dashboard/director_student_details.html')

def director_project_details(request):
    project = project_details.objects.all()
    context = {
        'project': project,
    }
    return render(request,'director_dashboard/director_project_details.html',context)

def director_guide_details(request):
    pi = Principal_investigator.objects.all()
    coi = Co_Investigator.objects.all()
    context = {
        'pi' : pi,
    }
    return render(request,'director_dashboard/director_guide_details.html',context)

def director_secretariat_details(request):
    sec = sec_details.objects.all()
    context = {
        'sec': sec
    }
    return render(request,'director_dashboard/director_secretariat_details.html',context)
def project_approval(request):
    project = project_details.objects.all()
    context = {
        'project': project,
    }
    return render(request,'director_dashboard/director_project_approval.html',context)

def project_approved(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 4
    std.is_initreview_done = True
    std.save()
    return redirect('director:project_approval')

def project_modified(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 0
    std.save()
    return render(request,'director_dashboard/modify.html')