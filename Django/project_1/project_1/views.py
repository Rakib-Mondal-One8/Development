from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>Home Page</h1>")
def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")