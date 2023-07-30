from django.shortcuts import render, redirect
from .models import Simulado, Pergunta
from .forms import RespostaForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Simuladao/index.html')

def lista_simulados(request):
    simulado = Simulado.objects.all()
    return render(request, 'Simuladao/listar_simulado.html', {'simulado': simulado})

@login_required
def realizar_simulado(request, simulado_id):
    # Resto da sua view...

    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            respostas_usuario = form.cleaned_data
            pontuacao_total = 0

            for questao in Pergunta:
                resposta_usuario = respostas_usuario.get(str(questao.id))
                if resposta_usuario == questao.resposta_correta:
                    pontuacao_total += questao.pontuacao

            # Salvar a pontuação total do usuário, se necessário
            if request.user.is_authenticated:
                user = request.user
                # Exemplo para associar a pontuação ao usuário logado
                user.profile.pontuacao_total = pontuacao_total
                user.profile.save()

            return redirect('mostrar_resultados', simulado_id=simulado_id)
    else:
        form = RespostaForm()

    return render(request, 'realizar_simulado.html', {'simulado': Simulado, 'questoes': Pergunta, 'form': form})

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

