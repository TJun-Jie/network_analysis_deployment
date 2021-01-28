from django import forms
from django.contrib.auth.models import User

class InputForm(forms.Form):    
    error_css_class = 'error'
    users = User.objects.all()
    friend1 = forms.ModelChoiceField(queryset=users.filter(is_staff=False).order_by('first_name'), required=True)
    friend2 = forms.ModelChoiceField(queryset=users.filter(is_staff=False).order_by('first_name'), required=True)
    friend3 = forms.ModelChoiceField(queryset=users.filter(is_staff=False).order_by('first_name'),required=True)

    def clean(self):
        all_clean_data = super().clean()
        
        friend1 = all_clean_data['friend1']
        friend2 = all_clean_data['friend2']
        friend3 = all_clean_data['friend3']
        if(friend1 == friend2 or friend2 == friend3 or friend3 == friend1):
            raise forms.ValidationError("Please do not enter the same person more than once")
        # if(student == friend1 or student == friend2 or student == friend3):
        #     raise forms.ValidationError("Please do not put your own name under the friend input")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name' ,'username','password')