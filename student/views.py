from django.shortcuts import render, redirect

# Create your views here.
from project.models import project_details
from student.forms import AddDocument, ReviewForm
from student.models import Std_details, Document
from users.models import CustomUser


def routing_logic(request):
    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    student = student[0]
    if(student.st_project_status==0):
        return redirect('project:project')
    else:
        return redirect('student:student_dashboard')


def student_dashboard(request):
    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    project = project_details.objects.filter(stud_id__in=Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username))))
    customuser = CustomUser.objects.filter(username=str(request.user.username))
    student= student[0]
    project = project[0]
    customuser = customuser[0]
    print(project.PI_id)
    context = {
        'student':student,
        'project':project,
        'cuser':customuser,
    }
    return render(request,'student_dashboard/student_dashboard.html',context)

def student_profile(request):
    std = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=request.user.username))
    #  sec = sec_details.objects.all()
    print(std)
    # std = std[0]
    context = {
        'std': std
    }
    return render(request, 'student_dashboard/student_profile.html', context)

def student_budget(request):
    return render(request,'student_dashboard/student_budget.html')

def student_project_details(request):
    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    project = project_details.objects.filter(stud_id__in=Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username))))
    customuser = CustomUser.objects.filter(username=str(request.user.username))
    student= student[0]
    project = project[0]
    customuser = customuser[0]
    print(project.PI_id)
    context = {
        'student':student,
        'project':project,
        'cuser':customuser,
    }
    return render(request,'student_dashboard/student_project_details.html',context)

def student_completion_report(request):
    return render(request,'student_dashboard/student_completion_report.html')

def viewdocuments(request):
    documents = Document.objects.all()
    context ={
        'documents':documents,
    }
    return render(request,'student_dashboard/student_documents.html',context)

def uploadDocuments(request):
    doc_form = AddDocument()

    if request.POST:
        doc_form = AddDocument(request.POST,request.FILES)


        if doc_form.is_valid():
            form1 = doc_form.save(commit=False)


            student = Std_details.objects.filter(
                student_id__in=CustomUser.objects.filter(username=str(request.user.username))
            )
            student = student[0]

            form1.student_id = student
            form1.save()
            doc_form = AddDocument()

    context = {
        'form' : doc_form,
    }
    return render(request,'student_dashboard/addDocument.html',context=context)


def sample(request):
    rev_form = ReviewForm()

    if request.POST:
        rev_form = ReviewForm(request.POST)

    if rev_form.is_valid():
        form1 = rev_form.save()


    context={'form1':rev_form}

    return render(request, "student_dashboard/forms.html", context)

