from django.db import models
from django.urls import reverse

# Criando model funcao.
class Horario(models.Model):
    descricao = models.CharField(max_length=50, help_text="Descrição do horário")
    hora_entrada = models.TimeField(max_length=4, help_text="Hora de entrada", null=True, blank=True)
    hora_saida = models.TimeField(max_length=5, help_text="Hora de saida", null=True, blank=True)
    intervalo_saida = models.TimeField(max_length=5, help_text="Hora de saída do intervalo", null=True, blank=True)
    intervalo_entrada = models.TimeField(max_length=5, help_text="Hora de entrada do intervalo", null=True, blank=True)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('lista_horarios')