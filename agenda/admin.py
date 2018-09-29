from django.contrib import admin
from .models import Paciente, Veiculo, Cidade, Motorista, AgendarConsulta
# Register your models here.

admin.site.register(Paciente)

admin.site.register(Veiculo)

admin.site.register(Cidade)
admin.site.register(AgendarConsulta)
admin.site.register(Motorista)
