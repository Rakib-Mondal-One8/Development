from django.urls import path
from . import views
urlpatterns = [
    path('',views.first_app),
   path('courses/',views.courses),
    path('about/',views.about),
]