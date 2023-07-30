from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import lista_simulados, index, realizar_simulado

app_name = 'simuladao'
urlpatterns = [
    path('', index, name='index'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('listar_simulados/', lista_simulados, name='lista_simulados'),
    path('realizar_simulado/<int:simulado_id>/', realizar_simulado, name='realizar_simulado'),
]
