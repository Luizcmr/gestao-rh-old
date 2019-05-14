from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from .forms import FuncionarioForm



#@login_required
#def funcionarios_update(request, id):
#    funcionario = get_object_or_404(Funcionario, pk=id)
#    form = FuncionarioForm(request.POST or None, request.FILES or None, instance=funcionario)
#
#    if form.is_valid():
#        form.save()
#        return redirect('funcionario_list')
#
#    return render(request, 'funcionario_form.html', {'form': form})


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','cpf','data_nasc','nacionalidade','naturalidade', 'sexo',
              'estado_civil','nome_conjuge','nome_pai','nome_mae','num_dependentes',
              'endereco','numero','complemento','bairro','cidade','uf','cep',
              'telefone','celular','email','rg','orgao','data_emissao','cnh',
              'pis','data_pis','banco_pis','ag_pis','ctps','ctps_rural',
              'titulo','zona','secao','cert_militar',
              'contato1','tel_contato1','contato2','tel_contato2',
              'cbo','data_admissao','salario','estrangeiro','casado_bras',
              'tem_filhos_bras','qtd_filhos_bras','data_chegada',
              'naturalizado','num_decreto','foto',
              'user','departamentos','funcao','empresa']

    def form_valid(self, form):
        obj = form.save()

        # gravando usuário no cadastro de funcionario
        # funcionario = self.request.user.funcionario
        # funcionario.funcionario = obj
        # funcionario.save()
        return redirect('lista_funcionarios')


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'data_nasc', 'nacionalidade', 'naturalidade', 'sexo',
              'estado_civil', 'nome_conjuge', 'nome_pai', 'nome_mae', 'num_dependentes',
              'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep',
              'telefone', 'celular', 'email', 'rg', 'orgao', 'data_emissao', 'cnh',
              'pis', 'data_pis','banco_pis', 'ag_pis', 'ctps', 'ctps_rural',
              'titulo', 'zona', 'secao', 'cert_militar',
              'contato1', 'tel_contato1', 'contato2', 'tel_contato2',
              'cbo', 'data_admissao', 'salario', 'estrangeiro', 'casado_bras',
              'tem_filhos_bras', 'qtd_filhos_bras', 'data_chegada',
              'naturalizado', 'num_decreto', 'foto',
              'user', 'departamentos', 'funcao', 'empresa']



class FuncionarioList(ListView):
    model = Funcionario
    fields = ['nome', 'cpf', 'data_nasc', 'nacionalidade', 'naturalidade', 'sexo',
              'estado_civil', 'nome_conjuge', 'nome_pai', 'nome_mae', 'num_dependentes',
              'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep',
              'telefone', 'celular', 'email', 'rg', 'orgao', 'data_emissao', 'cnh',
              'pis', 'data_pis', 'banco_pis', 'ag_pis', 'ctps', 'ctps_rural',
              'titulo', 'zona', 'secao', 'cert_militar',
              'contato1', 'tel_contato1', 'contato2', 'tel_contato2',
              'cbo', 'data_admissao', 'salario', 'estrangeiro', 'casado_bras',
              'tem_filhos_bras', 'qtd_filhos_bras', 'data_chegada',
              'naturalizado', 'num_decreto', 'foto',
              'user', 'departamentos', 'funcao', 'empresa']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("lista_funcionarios")