from django import forms

class FormPaciente(forms.Form):
   nome = forms.CharField(label='Nome', max_length=1000)
   rg = forms.CharField(max_length=20)
   cpf = forms.CharField(max_length=20)
   telefone = forms.CharField(max_length=20)
   email = forms.EmailField(max_length=200)


class FormVeiculo(forms.Form):
   placa = forms.CharField(label='Nome', max_length=1000)
   modelo = forms.CharField(max_length=20)
   cor = forms.CharField(max_length=20)
   capacidade = forms.CharField(max_length=20)
   disponivel = forms.BooleanField()