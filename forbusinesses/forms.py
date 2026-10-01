from django import forms
from .models import BusinessRegistration


class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = BusinessRegistration
        fields = '__all__'