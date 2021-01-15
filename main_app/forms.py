from django import forms
from .models import Student

class InputForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend1 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend2 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend3 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))

