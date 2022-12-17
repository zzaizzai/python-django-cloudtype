from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("name", 'address', 'phone', 'web', 'email_address')

        # labels = {
        #     'name': 'name',
        #     'address': 'address',
        #     'phone': 'phone',
        #     'web': 'web',
        #     'email_address': 'email_address',

        # }

        labels = {
            'name': '',
            'address': '',
            'phone': '',
            'web': '',
            'email_address': '',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'web URL'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email_address'}),

        }
