from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Your Phone'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
        }