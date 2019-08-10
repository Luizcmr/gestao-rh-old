from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from apps.movimentacoes.models import Movimentacao
from .forms import FuncionarioForm


class FuncionarioCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'funcionarios.add_funcionario'
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


class FuncionarioEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'funcionarios.change_funcionario'
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
              'departamentos', 'funcao', 'empresa']



class FuncionarioList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'funcionarios.view_funcionario'
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
              'departamentos', 'funcao', 'empresa']

    def get_queryset(self):
        filter_nome = self.request.GET.get('pesqnome', None)
        filter_cpf = self.request.GET.get('pesqcpf', None)
        order = 'nome'
        if filter_nome:
            new_context = Funcionario.objects.filter(nome__icontains=filter_nome, ).order_by(order)
        else:
            if filter_cpf:
               new_context = Funcionario.objects.filter(cpf__icontains=filter_cpf, ).order_by(order)
            else:
               new_context = Funcionario.objects.order_by(order).all()
        return new_context


class FuncionarioDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'funcionarios.delete_funcionario'
    model = Funcionario
    success_url = reverse_lazy("lista_funcionarios")


class FuncionarioTransfere(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'funcionarios.change_funcionario'
    model = Funcionario
    fields = ['nome', 'cpf', 'empresa', 'data_movto']
    template_name_suffix = '_transferir'

    def form_valid(self, form):

        """If the form is valid, save the associated model."""
        func = form.save(commit=False)

        # Salvando dados da transferencia em movimentação do funcionario
        obs = "Funcionário transferido para empresa " + str(func.empresa)
        mov = Movimentacao.objects.create(funcionario_id=func.id,
                                          data_evento=func.data_movto,
                                          data_para_conclusao=func.data_movto,
                                          concluido_em=func.data_movto,
                                          evento_id=4,
                                          observacao=obs
                                          )
        self.object = form.save()
        return super().form_valid(form)