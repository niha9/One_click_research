from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect

# Create your views here.
from project.models import project_details, sec_details
from student.models import Std_details
from untitled300 import settings
from users.models import CustomUser


def secretariat_dashboard(request):
    project = project_details.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'secretariat_dashboard/sec_dashboard.html', context)

# Create your views here.

def email(request,pk):
     subject = 'welcome to pd hinduja research centre'
     from_email = settings.EMAIL_HOST_USER
     message = 'hey congrats your paper has been approved'
     reciepent =['prashantkapri7@gmail.com']
     to_email = [settings.EMAIL_HOST_USER,'prashantkapri7@gmail.com']
     try:
       send_mail(subject, message, from_email, to_email,fail_silently=False)
     except BadHeaderError:
       return HttpResponse('Invalid header found.')
     return redirect('secretariat:secretariat_dashboard')

def thanks(request):
    return HttpResponse('Thank you for your message.')

def secretariat_profile(request, ):
    sec = sec_details.objects.filter(sec_id__in=CustomUser.objects.filter(username=request.user.username))
    # sec = sec_details.objects.all()
    print(sec)
    sec = sec[0]
    context = {
        'sec': sec
    }
    return render(request, 'secretariat_dashboard/sec_profile.html', context)

def secretariat_director_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_director_review.html',context)

def secretariat_irb_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_irb_review.html',context)

def secretariat_final_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_final_review.html',context)






def upstatdr(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 3
    std.save()
    return render(request,'secretariat_dashboard/modify.html')

def upstatirbr(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 3
    std.save()
    return render(request,'secretariat_dashboard/modify.html')

def upstatfin(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 10
    std.save()
    return render(request,'secretariat_dashboard/modify.html')
