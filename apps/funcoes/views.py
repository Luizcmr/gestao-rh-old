from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Funcao


class FuncaoCreate(CreateView):
    model = Funcao
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_funcoes')


class FuncaoEdit(UpdateView):
    model = Funcao
    fields = ['nome']

class FuncaoList(ListView):
    model = Funcao
    fields = ['nome']

class FuncaoDelete(DeleteView):
    model = Funcao
    success_url = reverse_lazy("lista_funcoes")