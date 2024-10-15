from django.shortcuts import render,redirect
from . import models
from firstapp.forms import StudentForm
def home(request):
    # student = models.Student.objects.all()
    # print(student)
    # return render(request,'home.html',{'student':student})
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()

    return render(request,'home.html',{'form':form})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('home')
