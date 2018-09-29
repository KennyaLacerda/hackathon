from django.urls import path
from . import views

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_paciente/', views.cadastro_paciente, name='cadastro_paciente'),
    path('cadastro_veiculo/', views.veiculo, name='cadastro_veiculo'),


    path('sucesso/', views.sucesso, name='sucesso'),

    #path('principal', views.principal, name='principal'),

   
   

]