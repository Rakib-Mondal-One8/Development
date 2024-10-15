from django.contrib import admin
from firstapp.models import StudentModel
from . import models
admin.site.register(models.Student)
admin.site.register(StudentModel)
