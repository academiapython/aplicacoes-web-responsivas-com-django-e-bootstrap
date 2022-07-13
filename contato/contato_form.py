from django.forms import ModelForm
from django import forms
from contato.models import Contato

class FormContato(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
            'assunto': forms.Select(attrs={'class': 'form-control form-select mb-3'}),
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }
