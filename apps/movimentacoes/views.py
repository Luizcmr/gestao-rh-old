import io

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from xlwt import easyxf
from datetime import datetime
from django.views import View
from .models import Movimentacao, Funcionario
import xlwt

class MovimentacaoCreate(CreateView):
    model = Movimentacao
    fields = ['funcionario', 'evento', 'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao','arquivo_mov']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_movimentacoes')

class MovimentacaoEdit(UpdateView):
    model = Movimentacao
    fields = ['funcionario', 'evento',  'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao','arquivo_mov']


class MovimentacaoList(ListView):
    model = Movimentacao
    fields = ['funcionario', 'evento',  'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao','arquivo_mov']

    def get_queryset(self):
        filter_func = self.request.GET.get('pesqfunc', None)
        filter_evento = self.request.GET.get('pesqevento', None)
        order = ('funcionario')
        if filter_func:
            new_context = Movimentacao.objects.filter(funcionario__nome__icontains=filter_func, )
        else:
            if filter_evento:
                new_context = Movimentacao.objects.filter(evento__nome__icontains=filter_evento, )
            else:
                new_context = Movimentacao.objects.all()
        return new_context


class MovimentacaoDelete(DeleteView):
    model = Movimentacao
    success_url = reverse_lazy("lista_movimentacoes")

class EventosAVencer(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'movimentacoes.view_movimentacao'
    template_name_suffix = '_a_vencer'
    model = Movimentacao
    fields = ['funcionario', 'evento', 'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao','arquivo_mov']

    def get_queryset(self):
        order = 'data_para_conclusao'
        ddata = datetime.now()
        new_context = Movimentacao.objects.filter(data_para_conclusao__gt=ddata,).order_by(order)
        return new_context


class EventosAVencerExcel(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'movimentacoes.view_movimentacao'

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Eventos-A-Vencer.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('A Vencer')

        row_num = 0

        ws.col(0).width = 10000
        ws.col(1).width = 4000
        ws.col(2).width = 4000
        ws.col(3).width = 4000
        ws.col(4).width = 4000

        style_border = easyxf('border: bottom thin, left thin, top thin, right thin;'
                              'pattern: pattern solid, fore_colour black;'
                              'font: color white')

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        ddata = datetime.now()
        ws.write(row_num, 0, ddata.strftime('%d/%m/%Y %H:%M'), font_style)
        ws.write(row_num, 1, 'Sistema Gestão de RH', font_style)
        row_num = 2
        ws.write(row_num, 0, 'Eventos a Vencer', font_style)
        row_num = 4
        columns = ['Funcionário', 'Empresa', 'Evento', 'Data do Evento', 'Data Vencimento']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], style_border)

        font_style = xlwt.XFStyle()

        order = 'data_para_conclusao'
        ddata = datetime.now()
        registros = Movimentacao.objects.filter(data_para_conclusao__gt=ddata, ).order_by(order)

        row_num = 5
        for registro in registros:
            ws.write(row_num, 0, registro.funcionario.nome, font_style)
            ws.write(row_num, 1, registro.funcionario.empresa.nome, font_style)
            ws.write(row_num, 2, registro.evento.nome, font_style)
            ws.write(row_num, 3, registro.data_evento.strftime('%d/%m/%Y'), font_style)
            ws.write(row_num, 4, registro.data_para_conclusao.strftime('%d/%m/%Y'), font_style)
            row_num += 1

        wb.save(response)
        return response


class EventosAVencerPDF(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'movimentacoes.view_movimentacao'

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Eventos-A-Vencer.pdf"'
        ddata = datetime.now()

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont('Helvetica', 10)

        p.drawString(20, 810, ddata.strftime('%d/%m/%Y '))
        p.drawString(((530-16)/2), 800, 'Eventos a Vencer')
        p.drawString(520, 810, ddata.strftime('%H:%M'))

        p.setFont('Helvetica', 8)

        p.drawString(20, 770, 'Funcionário')
        p.drawString(200, 770, 'Empresa')
        p.drawString(380, 770, 'Evento')
        p.drawString(460, 770, 'Data Evento')
        p.drawString(520, 770, 'Vencimento')

        p.drawString(0, 760, '_' * 150)

        order = 'data_para_conclusao'
        ddata = datetime.now()
        registros = Movimentacao.objects.filter(data_para_conclusao__gt=ddata, ).order_by(order)

        y = 740
        cEmpresaAnt = " "
        for registro in registros:
            p.drawString(20, y, (registro.funcionario.nome))
            p.drawString(200, y, (registro.funcionario.empresa.nome))
            p.drawString(380, y, (registro.evento.nome))
            p.drawString(460, y, (registro.data_evento.strftime('%d/%m/%Y')))
            p.drawString(520, y, (registro.data_para_conclusao.strftime('%d/%m/%Y')))
            y -= 20

        p.showPage()
        p.save()

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response
