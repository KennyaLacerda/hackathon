from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Paciente, Veiculo, Cidade, Motorista
from .forms import FormPaciente, FormVeiculo, FormCidade, FormMotorista
# Create your views here.
def index(request):
	return render(request, 'agenda/index.html')


def cadastro_paciente(request):
	if request.method == 'POST':
		form = FormPaciente(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			m = Paciente()
			m.nome = form.cleaned_data['nome']
			m.rg = form.cleaned_data['rg']
			m.cpf = form.cleaned_data['cpf']
			m.telefone = form.cleaned_data['telefone']
			m.email = form.cleaned_data['email']
			m.save()
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormPaciente() 

		contexto = {"form": form}
		return render(request, 'agenda/cadastro_paciente.html', contexto)

def cadastro_veiculo(request):
	if request.method == 'POST':
		form = FormVeiculo(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			m = Veiculo()
			m.placa = form.cleaned_data['placa']
			m.modelo = form.cleaned_data['modelo']
			m.cor = form.cleaned_data['cor']
			m.capacidade = form.cleaned_data['capacidade']
			m.disponivel = form.cleaned_data['disponivel']
			m.save()
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormVeiculo() 

		contexto = {"form": form}
		return render(request, 'agenda/cadastrar_veiculo.html', contexto)

def cadastro_cidade(request):
	if request.method == 'POST':
		form = FormCidade(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			m = Cidade()
			m.cidade = form.cleaned_data['cidade']
			m.estado = form.cleaned_data['estado']
			m.cep = form.cleaned_data['cep']
			m.save()
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormCidade() 

		contexto = {"form": form}
		return render(request, 'agenda/cadastro_cidade.html', contexto)

def cadastro_motorista(request):
	if request.method == 'POST':
		form = FormMotorista(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			m = Motorista()
			m.nome = form.cleaned_data['nome']
			m.cpf = form.cleaned_data['cpf']
			m.telefone = form.cleaned_data['telefone']
			m.save()
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormMotorista() 

		contexto = {"form": form}
		return render(request, 'agenda/cadastro_motorista.html', contexto)



def sucesso(request): 
   msg = "Cadastrada com Sucesso!" 
   contexto = {"msg": msg} 
   return render(request, 'agenda/sucesso.html', contexto)