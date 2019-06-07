from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from apps.empresas.models import Empresa
from apps.funcoes.models import Funcao
from apps.funcionarios.models import Funcionario

# Criando model funcionario.
class Contrato(models.Model):

   SN_CHOICES = (
       ('S', u'Sim'),
       ('N', u'Não'),
   )

   funcionario = models.ForeignKey(Funcionario, related_name='r_funcionario', on_delete=models.PROTECT, null=True, blank=True)
   empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
   contratado_por = models.ForeignKey(Funcionario, related_name='r_contratado_por', on_delete=models.PROTECT, null=True, blank=True)
   data_lancamento = models.DateField('criado em', auto_now_add=True)
   data_admissao = models.DateField(help_text="Data de Admissão", null=True, blank=True )
   data_registro = models.DateField(help_text="Data de Registro", null=True, blank=True )
   optante_fgts = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Optante FGTS(S/N)", null=True, blank=True)
   data_opcao = models.DateField(help_text="Data de Opção", null=True, blank=True )
   data_retratacao = models.DateField(help_text="Data de Retratação", null=True, blank=True )
   banco_depositario = models.CharField(max_length=3, help_text="Banco do FGTS", null=True, blank=True)
   em_experiencia = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Em experiência(S/N)", null=True, blank=True)
   prazo_experiencia = models.IntegerField(help_text="Prazo de Experiência", null=True, blank=True)
   vencto_experiencia = models.DateField(help_text="Vencimento da Experiência", null=True, blank=True )
   funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, null=True, blank=True)
   salario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salário", null=True, blank=True)
   data_inicio_aviso = models.DateField(help_text="Data de Início do Aviso", null=True, blank=True )
   data_fim_aviso = models.DateField(help_text="Data Final do Aviso", null=True, blank=True )
   motivo = models.CharField(max_length=100, help_text="Motivo da Demissão", null=True, blank=True)
   data_demissao = models.DateField(help_text="Data de Demissão", null=True, blank=True )
   data_homologacao = models.DateField(help_text="Data de Homologação", null=True, blank=True )
   data_pagamento = models.DateField(help_text="Data de Pagamento", null=True, blank=True )
   login = models.CharField(max_length=20, help_text="Motivo da Demissão", null=True, blank=True)
   data_mov = models.DateTimeField(auto_now_add=True, help_text="Data do Movimento")
   tipo_ope = models.CharField(max_length=1, help_text="Tipo de Operação", null=True, blank=True)


   def __str__(self):
       return self.funcionario

   def get_absolute_url(self):
       return reverse('lista_contratos')
