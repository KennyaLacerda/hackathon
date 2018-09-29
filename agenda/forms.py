from django import forms
from .models import Paciente, Cidade, Veiculo



#pacient = Paciente.objects.all()
#city = Cidade.objects.all()

class FormPaciente(forms.Form):
   nome = forms.CharField(label='Nome', max_length=1000)
   rg = forms.CharField(label='RG', max_length=20)
   cpf = forms.CharField(label='CPF', max_length=20)
   telefone = forms.CharField(label='Telefone', max_length=20)
   email = forms.EmailField(label='Email', max_length=200)


class FormVeiculo(forms.Form):
   placa = forms.CharField(label='Placa', max_length=1000)
   modelo = forms.CharField(label='Modelo', max_length=20)
   cor = forms.CharField(label='Cor', max_length=20)
   capacidade = forms.CharField(label='Capacidade', max_length=20)
   disponivel = forms.BooleanField(label='Disponível')



class FormCidade(forms.Form):
   cidade = forms.CharField(label='Cidade', max_length=1000)
   estado = forms.CharField(label='Estado', max_length=20)
   cep = forms.CharField(label='Cep', max_length=10)

class FormMotorista(forms.Form):
   nome = forms.CharField(label='Nome', max_length=1000)
   cpf = forms.CharField(label='CPF', max_length=20)
   telefone = forms.CharField(label='Telefone', max_length=15)



class FormAgendarConsulta(forms.Form):
   paciente = forms.ChoiceField(choices=[('0', '--Selecione--')]+    [(pacient.id, pacient.nome) for pacient in Paciente.objects.all()])
   cidade = forms.ChoiceField(choices=[('0', '--Selecione--')]+    [(city.id, city.cidade) for city in Cidade.objects.all()])

   local = forms.CharField(max_length=2000)
   #hora_consulta = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
   data = forms.DateField()
   tipo_de_consulta = forms.CharField(max_length=2000)


class FormAlocarVeiculos(forms.Form):  
   
   veiculo =forms.ChoiceField(choices=[('0', '--Selecione--')]+    [(carro.id, carro.placa) for carro in Veiculo.objects.all()])
   #cidade = forms.ChoiceField(choices=[('0', '--Selecione--')]+    [(city.id, city.cidade) for city in Cidade.objects.all()])
   #local = forms.CharField(max_length=2000)
   data = forms.DateField()
