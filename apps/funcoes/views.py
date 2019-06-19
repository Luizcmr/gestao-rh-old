from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Funcao


class FuncaoCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'funcoes.add_funcao'
    model = Funcao
    fields = ['nome','salario']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_funcoes')


class FuncaoEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'funcoes.edit_funcao'
    model = Funcao
    fields = ['nome','salario']

class FuncaoList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'funcoes.view_funcao'
    model = Funcao
    fields = ['nome','salario']

class FuncaoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'funcoes.delete_funcao'
    model = Funcao
    success_url = reverse_lazy("lista_funcoes")