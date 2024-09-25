# forms.py
from django import forms
from .models import Customer
from .models import Porcine
from .models import Breed
from .models import Feeding


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['identification', 'first_name', 'last_name', 'address', 'phone_number']

class PorcineForm(forms.ModelForm):
    class Meta:
        model = Porcine
        fields = ['identification', 'breed', 'age', 'weight', 'feeding', 'customer']

class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['breed_name']
class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['description', 'dosage']