from django import forms
from django.contrib.auth.models import User
from django import forms

class NameForm(forms.Form):
    transcript = forms.CharField(label='Enter the transcript')
    CHOICES = [('1', 'Female'), ('2', 'Male')]
    voice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
    		    'username', 
    		    'password', 
    		    'email', 
    		    'first_name', 
    		    'last_name'
    	] 


