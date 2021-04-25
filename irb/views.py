
from django.shortcuts import render, redirect

# Create your views here.
from guide.models import Principal_investigator
from project.models import project_details
from student.models import Std_details


def irb_dashboard(request):
    return render(request,'irb_dashboard/irb_dashboard.html')

def irb_approvals(request):
    g1 = project_details.objects.all()


    context = {
        "project": g1,
    }
    return render(request, 'irb_dashboard/irb_approvals.html',context)


def irb_minutes(request):
    return render(request,'irb_dashboard/irb_minutes_of_meeting.html')

def irb_approve(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 5
    std.save()
    return redirect('irb:irb_approvals')

def irb_modified(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 6
    std.save()
    return render(request,'irb_dashboard/modify.html')