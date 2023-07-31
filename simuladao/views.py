from django.shortcuts import render, redirect
from .models import Simulado, Pergunta, Alternativa
from .forms import RespostaForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Simuladao/index.html')

def lista_simulados(request):
    simulados = Simulado.objects.all()
    return render(request, 'Simuladao/listar_simulado.html', {'simulados': simulados})

@login_required
def realizar_simulado(request, simulado_id):
    # Obter o objeto do Simulado com base no ID (simulado_id)
    simulado = Simulado.objects.get(pk=simulado_id)

    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            # Processar o formulário e verificar as respostas do usuário
            respostas_usuario = form.cleaned_data['respostas']

            pontuacao_total = 0

            for pergunta_id, alternativa_id in respostas_usuario.items():
                pergunta = Pergunta.objects.get(pk=pergunta_id)
                alternativa_selecionada = Alternativa.objects.get(pk=alternativa_id)

                if alternativa_selecionada.alternativa_correta:
                    pontuacao_total += pergunta.pontuacao

            # Atualizar a pontuação total do usuário logado
            if request.user.is_authenticated:
                user = request.user
                user.profile.pontuacao_total += pontuacao_total
                user.profile.save()

            return redirect('mostrar_resultados', simulado_id=simulado_id)
    else:
        form = RespostaForm()

    # Obter as perguntas relacionadas ao simulado
    perguntas = simulado.pergunta.all()

    return render(request, 'realizar_simulado.html', {'simulado': simulado, 'questoes': perguntas, 'form': form})

def mostrar_resultados(request, simulado_id):
    simulado = Simulado.objects.get(id=simulado_id)
    questoes = Pergunta.objects.filter(simulado=simulado)
    total_questoes = questoes.count()

    # Recupere a pontuação do usuário, se necessário
    pontuacao = request.user.profile.pontuacao

    context = {
        'simulado': simulado,
        'questoes': questoes,
        'total_questoes': total_questoes,
        'pontuacao': pontuacao,
    }
    return render(request, 'mostrar_resultados.html', context)

