from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Departamento


class DepartamentoCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'departamentos.add_departamento'
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_departamentos')

class DepartamentoEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'departamentos.change_departamento'
    model = Departamento
    fields = ['nome']

class DepartamentoList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'departamentos.view_departamento'
    model = Departamento
    fields = ['nome']


class DepartamentoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'departamentos.delete_departamento'
    model = Departamento
    success_url = reverse_lazy("lista_departamentos")



