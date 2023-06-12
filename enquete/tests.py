import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Pergunta

def criar_pergunta(texto, dias):
        """Cria uma instância de pergunta com um dado enunciado e uma data"""
        data = timezone.now() + datetime.timedelta(days = dias)
        return Pergunta.objects.create(enunciado=texto, data_pub = data)

class DetalhesViewTeste(TestCase):
    def test_com_perguta_no_futuro(self):
        """ao tentar exibir os detalhes de pergunta no futuro recebemos 404"""
        pergunta = criar_pergunta('pergunta futura', 5)
        url =  reverse('enquete:detalhes', args=(pergunta.id,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)

class PerguntaModelTest(TestCase):
    def test_publicada_recentemente_com_pergunta_no_futuro(self):
        "ao acionar esse teste ele ira verificar se a pergunta publicada é no futuro"
        data = timezone.now() + datetime.timedelta(days=30)
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.was_published_recently(), False)

    def test_publicada_recentemente_com_pergunta_no_alem_das_48_horas(self):
        "ao acionar esse teste ele ira verificar se a pergunta publicada é passada (antes de 48h passadas)"
        data = timezone.now() - datetime.timedelta(hours = 48, seconds = 1)
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.was_published_recently(), False)

    def test_publicada_recentemente_com_pergunta_dentro_das_48_horas(self):
        "ao acionar esse teste ele ira verificar se a pergunta publicada é recente (dentro de 48h corridas)"
        data = timezone.now() - datetime.timedelta(hours = 47, minutes = 59, seconds = 59)
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.was_published_recently(), True)

class IndexViewTest(TestCase):
    '''def test_pergunta_com_data_futura(self):
        """Pergunta com data no futuro não será listada"""
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertContains(resposta, 'tem nenhuma enquete ainda não')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], [])'''

    def test_sem_perguntas_cadastradas(self):
        """Não havendo perguntas cadastradas é exibida uma menagem correspondente"""
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'tem nenhuma enquete ainda não')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], [])

    '''def test_pergunta_com_data_no_passado(self):
        """Pergunta com data no passado será listada normalmene"""
        criar_pergunta('Pergunta no passado', -1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], ['<Pergunta:Pergunta no passado>'])'''

    '''def test_com_pergunta_no_passado_outra_no_futuro(self):
        """Só devem ser exibidas perguntas com datas no passado"""
        criar_pergunta('Pergunta no passado', -1)
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], ['<Pergunta:Pergunta no passado>'])'''

    '''def test_com_duas_perguntas_no_passado(self):
        """As perguntas com datas no passado são exibidas ordenadas"""
        criar_pergunta('Pergunta no passado 1', -10)
        criar_pergunta('Pergunta no passado 2', -5)
        resposta = self.client.get(reverse('enquete:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], ['<Pergunta:Pergunta no passado 2>', '<Pergunta: Pergunta no passado 1>'])'''
