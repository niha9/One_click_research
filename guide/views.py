from django.shortcuts import render, redirect

# Create your views here.
from guide.models import Principal_investigator
from project.models import project_details
from student.models import Std_details
from users.models import CustomUser


def guide_dashboard(request):
    return render(request,'guide_dashboard/guide_dashboard.html')

def guide_profile(request):
    return render(request,'guide_dashboard/guide_profile.html')

def guide_student(request):
    g1=Principal_investigator.objects.get(principal_id=request.user)
    g2=project_details.objects.filter(PI_id=g1)

    context={
        "project":g2,
    }

    return render(request,'guide_dashboard/guide_student.html',context)

def update_stuff(request):
    std = Std_details.objects.all()
    std = std[1]

    std.st_project_status += 1
    std.save()
    return redirect('guide:guide_student')



def initreview(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 2
    std.save()
    return redirect('guide:guide_student')

def interreview(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 8
    std.save()
    return redirect('guide:guide_student')

def finalreview(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 10
    std.save()
    return redirect('guide:guide_student')

def initmodifychanges(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 0
    std.save()
    return render(request,'guide_dashboard/modify.html')

def intermodifychanges(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 6
    std.save()
    return redirect('guide:guide_student')