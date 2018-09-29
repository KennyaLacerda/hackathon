from django import forms

class FormPaciente(forms.Form):
   nome = forms.CharField(label='Nome', max_length=1000)
   rg = forms.CharField(max_length=20)
   cpf = forms.CharField(max_length=20)
   telefone = forms.CharField(max_length=20)
   email = forms.EmailField(max_length=200)


class FormVeiculo(forms.Form):
   placa = forms.CharField(label='placa', max_length=1000)
   modelo = forms.CharField(max_length=20)
   cor = forms.CharField(max_length=20)
   capacidade = forms.CharField(max_length=20)
   disponivel = forms.BooleanField()



class FormCidade(forms.Form):
   cidade = forms.CharField(label='cidade', max_length=1000)
   estado = forms.CharField(max_length=20)
   cep = forms.CharField(max_length=10)

class FormMotorista(forms.Form):
   nome = forms.CharField(label='nome', max_length=1000)
   cpf = forms.CharField(max_length=20)
   telefone = forms.CharField(max_length=15)

