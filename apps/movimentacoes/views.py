from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Movimentacao, Funcionario



class MovimentacaoCreate(CreateView):
    model = Movimentacao
    fields = ['funcionario', 'evento', 'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_movimentacoes')

class MovimentacaoEdit(UpdateView):
    model = Movimentacao
    fields = ['funcionario', 'evento',  'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao']


class MovimentacaoList(ListView):
    model = Movimentacao
    fields = ['funcionario', 'evento',  'data_evento',
              'data_para_conclusao', 'concluido_em', 'observacao']

    def get_queryset(self):
        filter_func = self.request.GET.get('pesqfunc', None)
        order = 'funcionario'
        if filter_func:
            new_context = Movimentacao.objects.filter(funcionario__nome__contains=filter_func, ).order_by(order)
        else:
            new_context = Movimentacao.objects.order_by(order).all()
        return new_context


class MovimentacaoDelete(DeleteView):
    model = Movimentacao
    success_url = reverse_lazy("lista_movimentacoes")