from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100, default='sections')
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=100,default='Rakib')
    def __str__(self):
        return f"Name : {self.name}  ||  Roll : {self.roll}"


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100,default='Rakib')
    address = models.TextField()
    def __str__(self):
        return f"Name : {self.name}  ||  Roll : {self.roll}"