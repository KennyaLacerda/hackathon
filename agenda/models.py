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


class Veiculo(models.Model):
	placa = models.CharField(max_length=2000)
	modelo = models.CharField(max_length=15)
	cor = models.CharField(max_length=15)
	capacidade = models.IntegerField(max_length=50)
	disponivel = models.BooleanField()
   
	def __str__(self):
		return self.placa

class Cidade(models.Model):
	cidade = models.CharField(max_length=2000)
	estado = models.CharField(max_length=15)
	cep = models.CharField(max_length=15)

	def __str__(self):
		return self.cidade


class Motorista(models.Model):
	nome = models.CharField(max_length=2000)
	cpf = models.CharField(max_length=15)
	telefone = models.CharField(max_length=15)

	def __str__(self):
		return self.nome