from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario
from apps.contratos.models import Contrato
from apps.beneficios.models import Beneficio

# Create your models here.
class Beneficios_func(models.Model):

    STATUS_CHOICES = (
        ('A', u'Ativo'),
        ('I', u'Inativo'),
        ('S', u'Suspenso'),
        ('B', u'Bloqueado'),
        ('C', u'Cancelado'),
        ('O', u'Outros'),
    )

    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT)
    beneficio = models.ForeignKey(Beneficio, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor do benefício", null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, help_text="Status", null=True, blank=True)

    def __str__(self):
        return self.valor

    def get_absolute_url(self):
        return reverse('edit_contrato', args=[self.contrato.id])