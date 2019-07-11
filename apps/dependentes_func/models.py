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
    cpf = models.CharField(max_length=14, help_text="cpf do dependente", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.cpf = chr_remove(self.cpf, ".-/")

        super(Dependentes_func, self).save(*args, **kwargs)

    @property
    def mcpf(self):
        return self.cpf[:3] + "." + self.cpf[3:6] + "." + self.cpf[6:9] + "-" + self.cpf[9:11]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.funcionario.id])

def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string