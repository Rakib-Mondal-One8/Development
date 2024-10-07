from django.shortcuts import render

def about(request):
    if (request.method == 'POST'):
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email,'select':select})
    return render(request, 'about.html')
def form(request):
    return render(request,'forms.html')
