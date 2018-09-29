from django.urls import path
from . import views

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_paciente/', views.cadastro_paciente, name='cadastro_paciente'),
    path('cadastro_veiculo/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('cadastro_cidade/', views.cadastro_cidade, name='cadastro_cidade'),
    path('cadastro_motorista/', views.cadastro_motorista, name='cadastro_motorista'),
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),




    path('sucesso/', views.sucesso, name='sucesso'),

    #path('principal', views.principal, name='principal'),

   
   

]