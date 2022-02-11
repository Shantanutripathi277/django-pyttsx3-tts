from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name')
    CHOICES = [('1', 'Female'), ('2', 'Male')]
    voice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    



