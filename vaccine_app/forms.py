from .models import Task
from django import forms

class Vaccinationforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['centre','dose','date']