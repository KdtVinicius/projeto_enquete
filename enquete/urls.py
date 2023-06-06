from django.urls import path
from . import views

app_name = 'enquete'
urlpatterns = [
    path('', views.IndexView.as_view(), name ='index'),

    path(
        'enquete/<int:pk>/detalhes/',
        views.DetalhesView.as_view(), name='detalhes'
    ),

    path(
        'enquete/<int:pk>/votacao/',
        views.VotacaoView.as_view(), name='votos'
    ),

    path(
        'enquete/<int:pk>/resultado/',
        views.ResultadoView.as_view(), name='resultado'
    ),

    path(
      'encerradas/',
      views.EncerradasView.as_view(), name = 'encerradas'
    ),

    ]