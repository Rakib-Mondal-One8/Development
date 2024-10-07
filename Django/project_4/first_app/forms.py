from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Name',initial='<NAME>', help_text='First name & Last name',required=False)
    # file = forms.FileField()
    # email = forms.EmailField(label='Email Address')
    # age = forms.IntegerField(label='Age')
    # Phone = forms.IntegerField(label='Phone Number')
    # weight = forms.FloatField(label='Weight')
    # balance = forms.DecimalField(label='Balance')
    # check = forms.BooleanField(label='Check')
    # date = forms.DateField(label='Date')
    # appointment = forms.SplitDateTimeField(label='Appointment')
    # CHOICES = [('S','SMALL'), ('M','MEDIUM'), ('L','LARGE')]
    # size = forms.ChoiceField(choices=CHOICES, label='Size')
    # meal = [('P','Pepperoni'),('M','Milk'),('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices=meal, label='Pizza')