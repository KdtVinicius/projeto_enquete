from django import forms
from .models import Pergunta, Simulado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RespostaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questoes = kwargs.pop('perguntas')  # Removendo 'perguntas' do kwargs
        super(RespostaForm, self).__init__(*args, **kwargs)
        for pergunta in questoes:
            alternativas = pergunta.alternativa_set.all()
            self.fields[f'pergunta_{pergunta.id}'] = forms.ChoiceField(
                choices=[(alternativa.id, alternativa.texto) for alternativa in alternativas],
                widget=forms.RadioSelect,
                label=pergunta.enunciado,
                required=False,
                initial=self.initial.get(f'pergunta_{pergunta.id}')  # Definindo as alternativas iniciais
            )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
