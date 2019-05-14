from django.forms import ModelForm
from django import forms
from .models import Funcionario
from localflavor.br.forms import BRCPFField


class FuncionarioForm(ModelForm):
    cpf = BRCPFField()
    class Meta:
        model = Funcionario
        fields = ['nome']
