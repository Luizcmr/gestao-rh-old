from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome','cnpj','fantasia','insc_est','insc_mun','endereco',
              'numero','complemento','bairro','cidade','uf','cep','telefones','email']

    def form_valid(self, form):
        obj = form.save()

        # gravando a empresa no funcionario que corresponde ao usuário
        # funcionario = self.request.user.funcionario
        # funcionario.empresa = obj
        # funcionario.save()
        return redirect('lista_empresas')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome', 'cnpj', 'fantasia', 'insc_est', 'insc_mun', 'endereco',
              'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'telefones', 'email']


class EmpresaList(ListView):
    model = Empresa
    fields = ['nome', 'cnpj', 'fantasia', 'insc_est', 'insc_mun', 'endereco',
              'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'telefones', 'email']

class EmpresaDelete(DeleteView):
    model = Empresa
    success_url = reverse_lazy("lista_empresas")