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

    path('alocar_veiculo/envio_data/', views.envio_data, name='envio_data'),

    path('envio_data_index/', views.envio_data_index, name='envio_data_index'),
    
    path('alocar_veiculo/', views.alocar_veiculo, name='alocar_veiculo'),
    path('alocar_veiculo/envio_data/<int:x>/alocar/', views.alocar, name='alocar'),

    path('<int:x>/add_veiculo/', views.add_veiculo, name='add_veiculo'),

    path('sucesso/', views.sucesso, name='sucesso'),

    path('relatorio/', views.relatorio, name='relatorio'),

    path('relatorio/ver_relatorio/', views.ver_relatorio, name='ver_relatorio'),

    #path('principal', views.principal, name='principal'),

   
   

]