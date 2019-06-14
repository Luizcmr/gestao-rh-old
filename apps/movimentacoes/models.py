from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario
from apps.eventos.models import Evento
from apps.empresas.models import Empresa

# Create your models here.
class Movimentacao(models.Model):

   funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=False, blank=False)
   evento = models.ForeignKey(Evento, on_delete=models.PROTECT, null=False, blank=False)
   data_lancamento = models.DateField('Lançado em', auto_now_add=True)
   data_evento = models.DateField(help_text="Data do Evento", null=True, blank=True)
   data_para_conclusao = models.DateField(help_text="Data para Conclusão", null=True, blank=True)
   concluido_em = models.DateField(help_text="Concluído em", null=True, blank=True)
   observacao = models.CharField(max_length=200, help_text="Observação", null=True, blank=True)
   login = models.CharField(max_length=20, help_text="login que lançou", null=True, blank=True)

   class Meta:
      ordering = ['funcionario','data_evento']

   #@property
   #def mempresa(self):
   #     return Empresa.objects.all()


   def __str__(self):
        return self.funcionario

   def get_absolute_url(self):
        return reverse('lista_movimentacoes')