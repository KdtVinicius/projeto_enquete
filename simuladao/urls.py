from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import lista_simulados, index

app_name = 'simuladao'
urlpatterns = [
    path('', index, name='index'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('realizar_simulado/', lista_simulados, name='realizar'),
]
