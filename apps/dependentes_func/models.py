from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario

# Criando model dependendes_func.
class Dependentes_func(models.Model):

    PARENTESCO_CHOICES = (
        ('C', u'Cônjuge OU Companheiro(a)'),
        ('F', u'Filho(a) ou enteado(a), até 21 anos'),
        ('E', u'Filho(a) ou enteado(a) Estudante, até 24 anos de idade'),
        ('I', u'Irmão(ã), neto(a) ou bisneto(a)'),
        ('A', u'Pais, avós e bisavós'),
        ('M', u'Menor pobre até 21 anos'),
        ('I', u'Pessoa absolutamente incapaz'),
        ('O', u'Outros'),
    )

    nome = models.CharField(max_length=50, help_text="Nome do dependente")
    parentesco = models.CharField(max_length=1, choices=PARENTESCO_CHOICES,  help_text="Grau de Parentesco", null=True, blank=True)
    data_nasc = models.DateField(help_text="emissao do pis", null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.funcionario.id])