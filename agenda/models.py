from django.db import models

# Create your models here.

class Paciente(models.Model):
	nome = models.CharField(max_length=2000)
	rg = models.CharField(max_length=15)
	cpf = models.CharField(max_length=15)
	telefone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.nome 
		#+ ': ' + self.rg + ': ' + self.cpf + ': '+ self.telefone + ': '+ self.email


class Veiculo(models.Model):
	#motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

	placa = models.CharField(max_length=2000)
	modelo = models.CharField(max_length=15)
	cor = models.CharField(max_length=15)
	capacidade = models.IntegerField(max_length=50)
	disponivel = models.BooleanField()

	def __str__(self):
		return 'Placa: ' + self.placa + ' | Modelo: ' + self.modelo + ' | Cor: ' + self.cor 

class Cidade(models.Model):
	cidade = models.CharField(max_length=2000)
	estado = models.CharField(max_length=15)
	cep = models.CharField(max_length=15)

	def __str__(self):
		return self.cidade 
		#+ ': ' + self.estado + ': ' + self.cep


class Motorista(models.Model):
	nome = models.CharField(max_length=2000)
	cpf = models.CharField(max_length=15)
	telefone = models.CharField(max_length=15)

	def __str__(self):
		return self.nome

class AgendarConsulta(models.Model):
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	local = models.CharField(max_length=2000)
	#hora_consulta = models.TimeField()
	data = models.DateField()
	tipo_de_consulta = models.CharField(max_length=2000)
	#def __str__(self):
		#return self.cidade 
		#+ ': ' + self.paciente + ': ' + self.local + ': '+ self.data + ': '+ self.tipo_de_consulta


#class CapacidadeVeiculo(models.Model):
#	Veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
#	agenda = models.ForeignKey(AgendarConsulta, on_delete=models.CASCADE)
#	qtd = models.IntegerField()
#	data_viagem = models.DateField()


class AlocarVeiculos(models.Model):
	veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
	agenda = models.ForeignKey(AgendarConsulta, on_delete=models.CASCADE)
	#capacidade = models.ForeignKey(CapacidadeVeiculo, on_delete=models.CASCADE)
	data_viagem = models.DateField()
	alocado = models.BooleanField()
	qtd_cabe = models.IntegerField()
    
	#def __str__(self):
		#return self.veiculo + ': ' + self.agenda + ': ' + self.data_viagem + ': '+ self.alocado + ': '+ self.qtd_cabe

		

		

   
