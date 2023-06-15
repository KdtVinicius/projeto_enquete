from django.urls import path
from . import views

app_name = 'projeto_enquete_disciplina'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

    ]