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

    def get_queryset(self):
        filter_nome = self.request.GET.get('pesqnome', None)
        filter_cnpj = self.request.GET.get('pesqcnpj', None)
        order = 'nome'
        if filter_nome:
            new_context = Empresa.objects.filter(nome__icontains=filter_nome, ).order_by(order)
        else:
            if filter_cnpj:
               new_context = Empresa.objects.filter(cnpj__icontains=filter_cnpj, ).order_by(order)
            else:
               new_context = Empresa.objects.order_by(order).all()

        return new_context

class EmpresaDelete(DeleteView):
    model = Empresa
    success_url = reverse_lazy("lista_empresas")