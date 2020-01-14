import io

from reportlab.pdfgen import canvas
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from xlwt import easyxf

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
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento','horario','data_inicio_horario']


class ContratoList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'contratos.view_contrato'
    model = Contrato
    fields = ['funcionario', 'empresa', 'contratado_por', 'data_admissao', 'data_registro',
              'optante_fgts', 'data_opcao', 'data_retratacao', 'banco_depositario', 'em_experiencia',
              'prazo_experiencia', 'vencto_experiencia', 'funcao', 'salario', 'data_inicio_aviso',
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento','horario','data_inicio_horario']

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
              'data_fim_aviso', 'motivo', 'data_demissao', 'data_homologacao', 'data_pagamento','horario','data_inicio_horario']

    def get_queryset(self):
        order = 'vencto_experiencia'
        ddata = datetime.now()
        new_context = Contrato.objects.filter(vencto_experiencia__gt=ddata,).order_by(order)
        return new_context

class ContratoEmExpExportarExcel(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'contratos.view_contrato'

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Contratos-Em-Experiencia.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Em Experiencia')

        row_num = 0

        ws.col(0).width = 10000
        ws.col(1).width = 10000
        ws.col(2).width = 4000
        ws.col(3).width = 4000
        ws.col(4).width = 2000
        ws.col(5).width = 4000

        style_border = easyxf('border: bottom thin, left thin, top thin, right thin;'
                              'pattern: pattern solid, fore_colour black;'
                              'font: color white')

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        ddata = datetime.now()
        ws.write(row_num, 0, ddata.strftime('%d/%m/%Y %H:%M'), font_style)
        ws.write(row_num, 1, 'Sistema Gestão de RH', font_style)
        row_num = 2
        ws.write(row_num, 0, 'Contrato de experiência a Vencer', font_style)
        row_num = 4
        columns = ['Funcionário', 'Empresa', 'Data Admissão', 'Em Experiência', 'Prazo', 'Vencimento']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], style_border)

        font_style = xlwt.XFStyle()

        order = 'vencto_experiencia'
        ddata = datetime.now()
        registros = Contrato.objects.filter(vencto_experiencia__gt=ddata, ).order_by(order)

        row_num = 5
        for registro in registros:
            ws.write(row_num, 0, registro.funcionario.nome, font_style)
            ws.write(row_num, 1, registro.funcionario.empresa.nome, font_style)
            ws.write(row_num, 2, registro.data_admissao.strftime('%d/%m/%Y'), font_style)
            ws.write(row_num, 3, registro.em_experiencia, font_style)
            ws.write(row_num, 4, registro.prazo_experiencia, font_style)
            ws.write(row_num, 5, registro.vencto_experiencia.strftime('%d/%m/%Y'), font_style)
            row_num += 1

        wb.save(response)
        return response


def load_funcionarios(request):
    id_empresa = 0
    funcionarios = Funcionario.objects.filter(empresa_id=id_empresa).order_by('nome')
    id_empresa = request.GET.get('empresa')
    funcionarios = Funcionario.objects.filter(empresa_id=id_empresa).order_by('nome')
    return render(request, 'hr/funcionario_dropdown_list_options.html', {'funcionarios': funcionarios})

class ContratoEmExpExportarPdf(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'contratos.view_contrato'

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Contratos-Em-Experiencia.pdf"'
        ddata = datetime.now()

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont('Helvetica',10)

        p.drawString(20, 810, ddata.strftime('%d/%m/%Y'))
        p.drawString(185, 800, 'Relatorio de Contrato em Experiência a Vencer')
        p.drawString(520, 810, ddata.strftime('%H:%M'))

        p.setFont('Helvetica', 8)

        p.drawString(20, 770, 'Funcionário')
        p.drawString(210, 770, 'Empresa')
        p.drawString(400, 770, 'Admissão')
        p.drawString(460, 770, 'Prazo')
        p.drawString(520, 770, 'Vencimento')

        p.drawString(0, 760, '_' * 150)

        order = 'vencto_experiencia'
        contratosemexp = Contrato.objects.filter(vencto_experiencia__gt=ddata,).order_by(order)

        y = 740

        for contrato in contratosemexp:
            p.drawString(20, y, (contrato.funcionario.nome))
            p.drawString(210, y, (contrato.empresa.nome))
            p.drawString(400, y, (contrato.data_admissao.strftime('%d/%m/%Y')))
            p.drawString(460, y, (str(contrato.prazo_experiencia)))
            p.drawString(520, y, (contrato.vencto_experiencia.strftime('%d/%m/%Y')))
            y -= 20

        p.showPage()
        p.save()

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response
