from django.shortcuts import render, redirect
from .models import Pergunta, Simulado, Profile
from .forms import RespostaForm

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

            # Associar as respostas e pontuação ao usuário logado
            if request.user.is_authenticated:
                user = request.user
                try:
                    profile = user.profile
                except Profile.DoesNotExist:
                    profile = Profile(user=user)
                profile.pontuacao_total = pontuacao_total
                profile.save()

            return redirect('mostrar_resultados', simulado_id=simulado_id)
    else:
        form = RespostaForm()

    return render(request, 'realizar_simulado.html', {'simulado': Simulado, 'questoes': Pergunta, 'form': form})
