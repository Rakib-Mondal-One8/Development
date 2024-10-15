from django.shortcuts import render
from . import models
def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request,'home.html',{'student':student})
