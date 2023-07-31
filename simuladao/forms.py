from django import forms
from .models import Alternativa

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = ['texto']
