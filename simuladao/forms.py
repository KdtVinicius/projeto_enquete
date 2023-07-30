from django import forms
from .models import Pergunta

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['resposta']
