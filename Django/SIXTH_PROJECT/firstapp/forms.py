from django import forms

from firstapp.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Roll Number'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
        help_texts = {
            'name' : 'Write Your Full Name',
        }
        error_messages = {
            'name' : {'required': 'Please enter your Full Name'},
        }