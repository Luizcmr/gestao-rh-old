from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Contrato, Funcionario


class ContratoCreate(CreateView):
    model = Contrato
    fields = ['funcionario','empresa','contratado_por','data_admissao','data_registro',
              'optante_fgts','data_opcao','data_retratacao','banco_depositario','em_experiencia',
              'prazo_experiencia','vencto_experiencia','funcao','salario','data_inicio_aviso',
              'data_fim_aviso','motivo', 'data_demissao','data_homologacao','data_pagamento']

    def form_valid(self, form):
        # gravando usuário no cadastro de contrato
        contrato = form.save(commit=False)
        v_login = 'teste'
        contrato.tipo_ope = 'I'
        contrato.login = v_login
        contrato.save()
        return redirect('lista_contratos')


class ContratoEdit(UpdateView):
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento']


class ContratoList(ListView):
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento']


class ContratoDelete(DeleteView):
    model = Contrato
    success_url = reverse_lazy("lista_contratos")