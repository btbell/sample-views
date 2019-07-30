from django import forms
from .models import DogForm

# a simple form using the Form class
class UserForm(forms.Form):
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(label='Last name', max_length=100)
  attend_date = forms.DateField(label='Date attending')
  email = forms.EmailField(label='Email')

class DogInfo(forms.ModelForm):

    class Meta:
        model = DogForm
        fields = ('pet_name', 'owner_last_name', 'attend_date', 'email')

