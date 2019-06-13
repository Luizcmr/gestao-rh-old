from django.db import models
from django.urls import reverse

# Criando model Evento.
class Evento(models.Model):
    id = models.IntegerField(primary_key=True, help_text="ID")
    nome = models.CharField(max_length=50, help_text="Nome do Evento")

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lista_eventos')