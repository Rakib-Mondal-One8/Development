from django.shortcuts import render
import datetime

def home(request):
    d = {'Author': 'Rakib', 'age': 18, 'lst': ['Python', 'is', 'Best'],'Today':datetime.datetime.now(),'val':"",'courses' : [
        {
            'id' :1,
            'name':'Python',
            'fee':5000
        },
        {
            'id' :2,
            'name':'Django',
            'fee':5000
        },
        {
            'id' :3,
            'name':'Flask',
            'fee':5000
        }
    ]}
    return render(request, 'home.html', d)
