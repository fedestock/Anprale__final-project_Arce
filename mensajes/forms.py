from django import forms
from django.contrib.auth.models import User
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
