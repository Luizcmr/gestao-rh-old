from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User

from apps.empresas.models import Empresa
from apps.funcoes.models import Funcao
from apps.funcionarios.models import Funcionario
from apps.movimentacoes.models import Movimentacao
from apps.horarios.models import Horario

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
   horario = models.ForeignKey(Horario, on_delete=models.PROTECT, null=True, blank=True)
   data_inicio_horario = models.DateField(help_text="Data de Início no Horário", null=True, blank=True )
   login = models.CharField(max_length=20, help_text="Motivo da Demissão", null=True, blank=True)
   data_mov = models.DateTimeField(auto_now_add=True, help_text="Data do Movimento")
   tipo_ope = models.CharField(max_length=1, help_text="Tipo de Operação", null=True, blank=True)

   class Meta:
       ordering = ['empresa','funcionario','data_lancamento']

   def save(self, *args, **kwargs ):

      # Atualizando dados do funcionario
      func = Funcionario.objects.filter(id=self.funcionario_id).update(salario=self.salario,
                                                                       funcao_id=self.funcao)

      # atualizando tabela de movimentacao do funcionario
      wdata_admissao = self.data_admissao
      wdata_aviso = self.data_inicio_aviso
      wdata_demissao = self.data_demissao

      if self.id != None and self.horario != None:
         contratoant = Contrato.objects.get(id=self.id)
         wdeschorarioant = contratoant.horario.descricao
         whorarioant = contratoant.horario_id
         wdatainicioant = contratoant.data_inicio_horario

         if whorarioant != self.horario_id:
            obs = "Horário Alterado de " + str(wdeschorarioant) + " para " + str(self.horario)
            wdata_concluido = (self.data_inicio_horario-timedelta(1))
            mov = Movimentacao.objects.create(funcionario=self.funcionario,
                                              evento_id=8,
                                              data_evento=self.data_inicio_horario,
                                              data_para_conclusao=self.data_inicio_horario,
                                              concluido_em=wdata_concluido,
                                              observacao=obs
                                             )

      if wdata_admissao is not None:
         movi_count = Movimentacao.objects.filter(evento=1, funcionario=self.funcionario_id).count()
         if movi_count == 0:
            obs = "Funcionário Admitido na empresa " + str(self.empresa)
            mov = Movimentacao.objects.create(funcionario=self.funcionario,
                                              evento_id=1,
                                              data_evento=wdata_admissao,
                                              data_para_conclusao=wdata_admissao,
                                              concluido_em=wdata_admissao,
                                              observacao=obs
                                              )

      if wdata_aviso is not None:
         movi_count = Movimentacao.objects.filter(evento=2, funcionario=self.funcionario_id).count()
         if movi_count == 0:
            obs = "Funcionário em Aviso Prévio na empresa " + str(self.empresa)
            mov = Movimentacao.objects.create(funcionario=self.funcionario,
                                              evento_id=2,
                                              data_evento=wdata_aviso,
                                              data_para_conclusao=wdata_aviso,
                                              concluido_em=wdata_aviso,
                                              observacao=obs
                                              )

      if wdata_demissao is not None:
         movi_count = Movimentacao.objects.filter(evento=3, funcionario=self.funcionario_id).count()

         if movi_count == 0:
            obs = "Funcionário Demitido da empresa " + str(self.empresa) + " pelo motivo " + str(self.motivo)
            mov = Movimentacao.objects.create(funcionario=self.funcionario,
                                              evento_id=3,
                                              data_evento=wdata_demissao,
                                              data_para_conclusao=wdata_demissao,
                                              concluido_em=wdata_demissao,
                                              observacao=obs
                                              )


      super(Contrato, self).save(*args, **kwargs)


   def __str__(self):
       return self.funcionario

   def get_absolute_url(self):
       return reverse('lista_contratos')
