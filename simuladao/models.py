from django.db import models
from django.contrib.auth.models import User

class Pergunta(models.Model):
    enunciado = models.CharField(max_length = 200)
    data_cadastro = models.DateTimeField('data de cadastro de questão')
    pontuacao = models.PositiveIntegerField(default = 0)
    resposta = models.CharField(max_length = 50, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.enunciado

    def total_de_votos(self):
        total = 0
        for alt in self.alternativa_set.all():
            total += alt.votos_quant
        return total

    def alternativas_ordenadas(self):
        return self.alternativa_set.order_by('-votos_quant')

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    texto = models.CharField(max_length = 100)
    votos_quant = models.IntegerField(default = 0)

    def __str__(self):
        return self.texto

    def porcentagem(self):
        return (self.votos_quant / self.pergunta.total_de_votos()) * 100

class Tema(models.Model):
    nome_tema = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome_tema

class Simulado(models.Model):
    nome_simulado = models.CharField(max_length = 100, default = 'digite o nome do seu simulado')
    pergunta = models.ManyToManyField(Pergunta)
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE)
    pontuacao = models.IntegerField(default = 0)
    data_pub = models.DateTimeField('data de publicação')
    data_fim = models.DateField('Data de encerramento', null = True)
    def __str__(self):
        return self.nome_simulado

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
