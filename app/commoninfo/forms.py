from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['id','Username','Password','Re_type','First_name','Last_name','DateOfBirth']
