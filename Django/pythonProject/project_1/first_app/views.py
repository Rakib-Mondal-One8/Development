from django.shortcuts import render
from django.http import HttpResponse

def first_app(request):
    return HttpResponse("First app Home Page")
def courses(request):
    return HttpResponse("This is the courses page (first_app)")
def about(request):
    return HttpResponse("This is the about page (first_app)")