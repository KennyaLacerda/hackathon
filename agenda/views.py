from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Paciente, Veiculo, Cidade, Motorista, AgendarConsulta, AlocarVeiculos
from .forms import FormPaciente, FormVeiculo, FormCidade, FormMotorista, FormAgendarConsulta, FormAlocarVeiculos
# Create your views here.




def relatorio(request):
	return render(request, 'agenda/relatorio.html')

def ver_relatorio(request):
	x = request.POST['data']
	lista = AlocarVeiculos.objects.filter(data_viagem = x)
	paciente = AgendarConsulta.objects.filter(data = x)
	contexto = {'lista':lista, 'paciente':paciente}
	return render(request, 'agenda/ver_relatorio.html', contexto)

def envio_data(request):
	x = request.POST['data']
	lista = AgendarConsulta.objects.filter(data =x)# retornar por data
	car = Veiculo.objects.all()
	form = FormAlocarVeiculos()
	contexto = {'lista':lista, 'car': car, 'form':form}
	return render(request, 'agenda/alocar_veiculo.html', contexto)


def envio_data_index(request):
	x = request.POST['data']
	lista = AgendarConsulta.objects.filter(data =x)# retornar por data	
	contexto = {'lista':lista}
	return render(request, 'agenda/index.html', contexto)

def alocar_veiculo(request):
	return render(request, 'agenda/alocar_veiculo.html')

def add_veiculo(request,x):
	return render(request, 'agenda/add_veiculo.html')

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


def alocar(request,x):
	if request.method == 'POST':
		form = FormAlocarVeiculos(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			
			m = AlocarVeiculos()
			#agenda = AgendarConsulta.objects.get(id = x)
			car = Veiculo.objects.get(id = form.cleaned_data['veiculo'])
			qtd = car.capacidade
			m.agenda = AgendarConsulta.objects.get(id = x)
			m.veiculo =car
			
			m.alocado = True
			m.qtd_cabe =  qtd-1
			m.data_viagem = form.cleaned_data['data']
			m.save() 
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormAlocarVeiculos() 
		lista = AgendarConsulta.objects.all()
		car = Veiculo.objects.all()

		contexto = {"form": form, 'lista':lista, 'car':car}
		return render(request, 'agenda/alocar_veiculo.html', contexto)

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


def agendar_consulta(request):
	if request.method == 'POST':
		form = FormAgendarConsulta(request.POST)
		if form.is_valid():           
        ### Salva a mensagem 
			m = AgendarConsulta()
			m.cidade =Cidade.objects.get(id = form.cleaned_data['cidade'])

			#form.cleaned_data['cidade']
			m.paciente = Paciente.objects.get(id = form.cleaned_data['paciente'])
			m.local = form.cleaned_data['local']
			m.hora_consulta = form.cleaned_data['hora_consulta']
			m.data = form.cleaned_data['data']
			m.tipo_de_consulta = form.cleaned_data['tipo_de_consulta']
			m.save()
			return HttpResponseRedirect('/agenda/sucesso')
		else:
			return HttpResponse("não encontrado" + str(request.POST)) 
	else:
		form = FormAgendarConsulta() 

		contexto = {"form": form}
		return render(request, 'agenda/agendar_consulta.html', contexto)



def sucesso(request): 
   msg = "Cadastrada com Sucesso!" 
   contexto = {"msg": msg} 
   return render(request, 'agenda/sucesso.html', contexto)