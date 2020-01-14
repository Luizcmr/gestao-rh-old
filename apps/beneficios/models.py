from django.db import models
from django.urls import reverse

# Criando model beneficio.
class Beneficio(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome do Benefício")

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lista_beneficios')