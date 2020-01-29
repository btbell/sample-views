from django import forms
from .models import DogInfo

# a simple form using the Form class

STATUS_CHOICES = [
  ('',''),
  ('s','Student'),
  ('p','Professional')
]
class UserForm(forms.Form):
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(label='Last name', max_length=100)
  attend_date = forms.DateField(label='Date attending')
  email = forms.EmailField(label='Email')
  #status = forms.CharField(label='Please choose whether a student or professional', max_length=12)
  status = forms.CharField(label='Please choose whether a student or professional.', initial='', widget=forms.Select(choices=STATUS_CHOICES))

class DogInfoForm(forms.ModelForm):

    class Meta:
        model = DogInfo
        fields = ('pet_name', 'owner_last_name', 'attend_date', 'email')

