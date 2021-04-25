from django.shortcuts import redirect, render
#from users.models import ,Std_details,Principal_investigator,sec_details,CustomUser
from users.models import *
from student.models import *
from guide.models import *
from secretariat.models import *
from director.models import *

def routing_logic(request):
    if(request.user.is_authenticated):


        if(request.user.type == 3):
            # student = Std_details.objects.filter(student_id__in = CustomUser.objects.filter(username= str(request.user.username )))
            # guidename = Principal_investigator.objects.filter(guide_id__in = CustomUser.objects.filter(username = student[0].guide))

            return redirect('student:route')
        elif(request.user.type == 0):
            return redirect('director:director_dashboard')
        elif(request.user.type == 1):
            return redirect('secretariat:secretariat_dashboard')
        elif(request.user.type == 2):
            return redirect('guide:guide_dashboard')
        elif(request.user.type == 4):
            return redirect('co_investigator:co_inv_dashboard')
        elif(request.user.type == 5):
            return redirect('irb:irb_dashboard')
        else:
            context = {
                'type' : 'coder',
            }
        return render(request, 'users/home.html', context=context)

    else:
        return redirect('login')
