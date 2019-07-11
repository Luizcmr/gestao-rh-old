
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Contrato, Funcionario
from .forms import ContratoForm
from datetime import datetime
import xlwt

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


class ContratoEmExp(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'contratos.view_contrato'
    template_name_suffix = '_em_experiencia'
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento']

    def get_queryset(self):
        order = 'vencto_experiencia'
        ddata = datetime.now()
        new_context = Contrato.objects.filter(vencto_experiencia__gt=ddata,).order_by(order)
        return new_context




class ContratoExportarExcel(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'contratos.view_contrato'

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Contratos-Em-Experiencia.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Em Experiencia')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        ddata = datetime.now()
        ws.write(row_num, 0, ddata.strftime('%d/%m/%Y'), font_style)
        ws.write(row_num, 2, 'Sistema Gestão de RH', font_style)
        row_num = 2
        ws.write(row_num, 0, 'Contrato de experiência a Vencer', font_style)
        row_num = 4

        columns = ['Funcionário', 'Data Admissão', 'Em Experiência', 'Prazo', 'Vencimento']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        order = 'vencto_experiencia'
        ddata = datetime.now()
        registros = Contrato.objects.filter(vencto_experiencia__gt=ddata, ).order_by(order)

        row_num = 5
        for registro in registros:
            ws.write(row_num, 0, registro.funcionario.nome, font_style)
            ws.write(row_num, 1, registro.data_admissao.strftime('%d/%m/%Y'), font_style)
            ws.write(row_num, 2, registro.em_experiencia, font_style)
            ws.write(row_num, 3, registro.prazo_experiencia, font_style)
            ws.write(row_num, 4, registro.vencto_experiencia.strftime('%d/%m/%Y'), font_style)
            row_num += 1

        wb.save(response)
        return response


def load_funcionarios(request):
    empresa_id = request.GET.get('empresa')
    funcionarios = Funcionario.objects.filter(empresa_id=empresa_id).order_by('nome')
    return render(request, 'hr/funcionario_dropdown_list_options.html', {'funcionarios': funcionarios})