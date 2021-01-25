from django import forms
from .models import Student
from django.contrib.auth.models import User


class InputForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend1 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend2 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))
    friend3 = forms.ModelChoiceField(queryset=Student.objects.all().order_by('name'))

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','username','email','password')