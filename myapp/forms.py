# forms.py
from django import forms
from .models import Customer
from .models import Porcine
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['identification', 'first_name', 'last_name', 'address', 'phone_number']

class PorcineForm(forms.ModelForm):
    class Meta:
        model = Porcine
        fields = ['identification', 'breed', 'age', 'weight', 'feeding', 'customer']
