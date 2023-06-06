from django.db import models
import datetime
from django.utils import timezone


class Pergunta(models.Model):
    enunciado = models.CharField(max_length = 200)
    data_pub = models.DateTimeField('data de publicação')
    data_fim = models.DateField('Data de encerramento', null = True)
    def __str__(self):
        return self.enunciado
    def total_de_votos(self):
        total = 0
        for alt in self.alternativa_set.all():
            total += alt.votos_quant
        return total
    def alternativas_ordenadas(self):
        return self.alternativa_set.order_by('-votos_quant')
    def was_published_recently(self):
        marco_48h = timezone.now() - datetime.timedelta(hours = 48)
        agora = timezone.now()
        return marco_48h <= self.data_pub <= agora
        #return(self.data_pub <= agora) and (self.data_pub >= marco_48h)

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    texto = models.CharField(max_length = 100)
    votos_quant = models.IntegerField(default = 0)
    def __str__(self):
        return self.texto
    def porcentagem(self):
        return (self.votos_quant / self.pergunta.total_de_votos()) * 100