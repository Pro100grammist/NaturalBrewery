from django import forms
from .models import CustomerRequestsDatabase


class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequestsDatabase
        fields = ['name', 'tel', 'email', 'comment']
