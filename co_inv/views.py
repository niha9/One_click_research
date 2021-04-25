from django.shortcuts import render

# Create your views here.


def co_inv_dashboard(request):
    return render(request,'co_inv_dashboard/co_inv_dashboard.html')

def co_inv_profile(request):
    return render(request,'co_inv_dashboard/co_inv_profile.html')

def co_inv_student(request):
    return render(request,'co_inv_dashboard/co_inv_student.html')

