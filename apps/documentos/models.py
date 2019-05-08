from django.db import models
from apps.funcionarios.models import Funcionario

# Criando model documentos.
class Documento(models.Model):
    descricao = models.CharField(max_length=50, help_text="Descrição do documento")
    id_func = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao