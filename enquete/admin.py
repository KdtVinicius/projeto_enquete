from django.contrib import admin
from .models import Pergunta, Alternativa

admin.site.site_header = 'Enquetes KdtVinicius 2023'

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 1

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adicione o enunciado da questão', {'fields':['enunciado']}),
        ('adicione as informações das datas', {'fields':['data_pub']}),
    ]
    inlines = [AlternativaInline]
    list_display= ('enunciado', 'id', 'data_pub', 'pubicada_recentemente')


admin.site.register(Pergunta, PerguntaAdmin)
