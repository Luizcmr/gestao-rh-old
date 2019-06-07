from django import forms
from .models import Contrato, Funcionario

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['empresa','funcionario','contratado_por','data_admissao','data_registro',
               'optante_fgts','data_opcao','data_retratacao','banco_depositario','em_experiencia',
               'prazo_experiencia','vencto_experiencia','funcao','salario','data_inicio_aviso',
               'data_fim_aviso','motivo', 'data_demissao','data_homologacao','data_pagamento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.none()