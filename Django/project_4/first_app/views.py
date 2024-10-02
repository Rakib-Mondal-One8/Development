from django.shortcuts import render

def index(request):
    d = {'l' : [1,2,3]}
    return render(request,'index.html',d)
