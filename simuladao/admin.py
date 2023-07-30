from django.contrib import admin
from .models import Pergunta, Simulado, Alternativa, Usuario, Tema
admin.site.site_header = 'Administração KdtVinicius 2023'

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [AlternativaInline]  # Adicionando a classe AlternativaInline como inline
    list_display = ('enunciado', 'data_cadastro', 'pontuacao')
    list_filter = ('data_cadastro', 'pontuacao')
    search_fields = ('enunciado',)

class SimuladoAdmin(admin.ModelAdmin):
    list_display = ('nome_simulado', 'data_pub', 'data_fim')
    list_filter = ('nome_simulado', 'data_pub', 'data_fim')
    search_fields = ('nome_simulado',)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome_tema',)

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Simulado, SimuladoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tema, TemaAdmin)