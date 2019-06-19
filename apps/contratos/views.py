from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Contrato, Funcionario
from .forms import ContratoForm


class ContratoCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'contratos.add_contrato'
    model = Contrato
    form_class = ContratoForm

    def form_valid(self, form):
        contrato = form.save(commit=False)
        v_login = 'teste'
        contrato.tipo_ope = 'I'
        contrato.login = v_login
        contrato.save()
        return redirect('lista_contratos')


class ContratoEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'contratos.edit_contrato'
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento']


class ContratoList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'contratos.view_contrato'
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento']

    def get_queryset(self):
        filter_func = self.request.GET.get('pesqfunc', None)
        filter_emp = self.request.GET.get('pesqemp', None)
        order = 'funcionario'
        if filter_func:
            new_context = Contrato.objects.filter(funcionario__nome__icontains=filter_func, ).order_by(order)
        else:
            if filter_emp:
               new_context = Contrato.objects.filter(empresa__nome__icontains=filter_emp, ).order_by(order)
            else:
               new_context = Contrato.objects.order_by(order).all()
        return new_context


class ContratoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'contratos.delete_contrato'
    model = Contrato
    success_url = reverse_lazy("lista_contratos")


def load_funcionarios(request):
    empresa_id = request.GET.get('empresa')
    funcionarios = Funcionario.objects.filter(empresa_id=empresa_id).order_by('nome')
    return render(request, 'hr/funcionario_dropdown_list_options.html', {'funcionarios': funcionarios})