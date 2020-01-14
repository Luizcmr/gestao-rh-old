from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario

# Criando model documentos.
class Documento(models.Model):
    descricao = models.CharField(max_length=50, help_text="Descrição do documento")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to="documentos")
    data_entrega = models.DateField(help_text="Data de Entrega", null=True, blank=True)
    data_vencimento = models.DateField(help_text="Data de Vencimento", null=True, blank=True)

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.funcionario.id])