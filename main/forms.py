from .models import Form
from django.forms import ModelForm, TextInput

class FormApp(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email']
        
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Name'
            }),
            "email": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            })
        }