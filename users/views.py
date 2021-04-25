from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from .forms import CustomGuideCreationForm, CustomStudentCreationForm

class SignUpGuide(generic.CreateView):
    form_class = CustomGuideCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class SignUpStudent(generic.CreateView):
    form_class = CustomStudentCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def readme(request):
    return render(request, '../templates/registration/readme.html')



