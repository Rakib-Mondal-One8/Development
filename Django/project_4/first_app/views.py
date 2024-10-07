from django.shortcuts import render
from  . forms import contactForm
def about(request):
    if (request.method == 'POST'):
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email,'select':select})
    return render(request, 'about.html')
def form(request):
    return render(request,'forms.html')

def DjangoForm(request):
    # if request.method == 'POST':
    #     form = contactForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         file = form.cleaned_data['file']
    #         with open('first_app/upload/'+file.name, 'wb+') as destination:
    #             for chunk in file.chunks():
    #                 destination.write(chunk)
    #         print(form.cleaned_data)
    # else:
    #     form = contactForm()
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django_form.html', {'form': form})