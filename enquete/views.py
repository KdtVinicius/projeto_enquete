from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from . models import Pergunta, Alternativa
from django.views import View
from django.utils import timezone

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista_perguntas = Pergunta.objects.filter(data_fim__gte = timezone.now()).order_by('-data_pub')
        #lista_perguntas = Pergunta.objects.filter(data_pub__lte = timezone.now()).order_by('-data_pub') isso aqui felipao mudou na aula de testes
        context = {'lista_perguntas': lista_perguntas}
        return render(request, 'enquete/index.html', context)

class EncerradasView(View):
    def get(self, request, *args, **kwargs):
        lista_perguntas = Pergunta.objects.filter(data_fim__lt = timezone.now()).order_by('-data_pub')
        context = {'lista_perguntas': lista_perguntas}
        return render(request, 'enquete/encerradas.html', context)

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        if pergunta.data_pub > timezone.now(): raise Http404('Nenhuma pergunta encontrada para essa especificação')
        return render(request, 'enquetes/pergunta_detail.html', {'pergunta': pergunta})

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        return render(request, 'enquete/resultado.html', {'pergunta': pergunta})


class VotacaoView(View):
    def post(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        try:
            id_alternativa = request.POST['choice']
            alt_selecionada = pergunta.alternativa_set.get(pk = id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'pergunta': pergunta,
                'error': 'você precisa selecionar uma alternativa válida'
                }
            return render(request, 'enquete/pergunta_detail.html', contexto)
        else:
            alt_selecionada.votos_quant += 1
            alt_selecionada.save()
            return HttpResponseRedirect(reverse(
                'enquete:resultado',
                args = (pergunta.id,)
                ))




'''

segunda versõa do index a primeira eu esqueci

def index(request):
    lista_perguntas = Pergunta.objects.all()
    template = loader.get_template('enquete/index.html')
    context = {'lista_perguntas': lista_perguntas}
    return HttpResponse(template.render(context, request))


terceira versão do index como função ainda:

def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    context = {'lista_perguntas': lista_perguntas}
    return render(request, 'enquete/index.html', context)


quarta versão index:

class IndexView(generic.ListView):
    template_name = 'enquete/index.html'
    context_object_name = 'lista_perguntas'
    def get_queryset(self):
        return Pergunta.objects.order_by('-data_pub')
------------------------------------------------------------------
primeria versão da view de resultados:

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquete/resultado.html', {'pergunta': pergunta})



segunda versão view de resultaods:

class ResultadoView(generic.DetailView):
    model = Pergunta
    template_name = 'enquete/resultado.html'

------------------------------------------------------------------
função de detalhes primeira versão
def detalhes(request, pergunta_id):
    try:
        pergunta = pergunta.objects.get(pk = pergunta_id)

    except PerguntaDoesNotExist:
        raise Http404("identificador de enquete inválido")

    return render(request, 'enquetes/index.html', {'pergunta': pergunta})


segunda versão da view de detalhes:
def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquete/detalhes.html', {'pergunta': pergunta})



terceira versão view de detalhes

class DetalheslView(generic.DetailView):
    model = Pergunta
------------------------------------------------------------------


'''