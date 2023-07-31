from django.shortcuts import render, redirect, get_object_or_404
from .models import Simulado, Pergunta, Alternativa, Usuario
from .forms import RespostaForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Simuladao/index.html')

def lista_simulados(request):
    simulados = Simulado.objects.all()
    return render(request, 'Simuladao/listar_simulado.html', {'simulados': simulados})

@login_required
def realizar_simulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)
    questoes = simulado.pergunta.all()
    total_perguntas = questoes.count()

    pontuacao_total = 0
    porcentagem_acertos = 0

    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            pontuacao_total = usuario.pontuacao_total
        except Usuario.DoesNotExist:
            # Tratar o caso em que o usuário não possui um perfil
            pontuacao_total = 0

    if request.method == 'POST':
        form = RespostaForm(questoes, request.POST)
        if form.is_valid():
            pontuacao = 0
            respostas_corretas = 0

            for questao in questoes:
                resposta_id = form.cleaned_data.get(f'pergunta_{questao.id}')
                if resposta_id is not None:
                    resposta = questao.alternativa_set.filter(id=resposta_id).first()
                    if resposta is not None and resposta.alternativa_correta:
                        pontuacao += 1
                        respostas_corretas += 1

            porcentagem_acertos = (respostas_corretas / total_perguntas) * 100

            # Atualize a pontuação total do usuário (caso exista) após submeter o formulário
            if request.user.is_authenticated:
                usuario.pontuacao_total = pontuacao
                usuario.save()

            context = {
                'simulado': simulado,
                'pontuacao_total': pontuacao_total,
                'total_perguntas': total_perguntas,
                'questoes': questoes,
                'porcentagem_acertos': porcentagem_acertos,
            }

            return render(request, 'mostrar_resultados.html', context)
    else:
        form = RespostaForm(questoes)

    context = {
        'simulado': simulado,
        'pontuacao_total': pontuacao_total,
        'total_perguntas': total_perguntas,
        'questoes': questoes,
        'porcentagem_acertos': porcentagem_acertos,
        'form': form,
    }

    return render(request, 'realizar_simulado.html', context)

def mostrar_resultados(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)
    questoes = simulado.pergunta.all()
    total_perguntas = questoes.count()

    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            pontuacao_total = usuario.pontuacao_total
        except Usuario.DoesNotExist:
            # Tratar o caso em que o usuário não possui um perfil
            pontuacao_total = 0
    else:
        # Tratar o caso em que o usuário não está autenticado
        pontuacao_total = 0

    porcentagem_acertos = (pontuacao_total / total_perguntas) * 100

    if request.method == 'POST':
        form = RespostaForm(request.POST, simulado_id=simulado_id)
        if form.is_valid():
            pontuacao = 0
            respostas_corretas = 0

            for questao in questoes:
                resposta_id = form.cleaned_data.get(f'pergunta_{questao.id}')
                if resposta_id is not None:
                    resposta = questao.alternativa_set.filter(id=resposta_id).first()
                    if resposta is not None and resposta.alternativa_correta:
                        pontuacao += 1
                        respostas_corretas += 1

            porcentagem_acertos = (respostas_corretas / total_perguntas) * 100

            # Atualize a pontuação total do usuário (caso exista) após submeter o formulário
            if request.user.is_authenticated:
                usuario.pontuacao_total = pontuacao
                usuario.save()

            context = {
                'simulado': simulado,
                'pontuacao_total': pontuacao_total,
                'total_perguntas': total_perguntas,
                'questoes': questoes,
                'porcentagem_acertos': porcentagem_acertos,
            }

            return render(request, 'mostrar_resultados.html', context)

    else:
        form = RespostaForm(simulado_id=simulado_id)

    context = {
        'simulado': simulado,
        'pontuacao_total': pontuacao_total,
        'total_perguntas': total_perguntas,
        'questoes': questoes,
        'porcentagem_acertos': porcentagem_acertos,
        'form': form,
    }

    return render(request, 'mostrar_resultados.html', context)

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('simuladao:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration_form.html', {'form': form})
