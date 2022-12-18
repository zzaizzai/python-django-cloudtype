from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name", 'event_date', 'venue',
                  'manager' , 'attendees' , 'description')

        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'event_date'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'venue'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'manager'}),
            
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),

        }


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
