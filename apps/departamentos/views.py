from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Departamento


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_departamentos')

class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoList(ListView):
    model = Departamento
    fields = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy("lista_departamentos")



