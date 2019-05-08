from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=14, help_text='CNPJ da empresa')
    fantasia = models.CharField(max_length=40, help_text='Nome fantasia', null=True, blank=True )
    endereco = models.CharField(max_length=60, help_text='Endereço', null=True, blank=True )
    insc_est = models.CharField(max_length=20, help_text='Inscrição Estadual', null=True, blank=True )
    insc_mun = models.CharField(max_length=20, help_text='Inscrição Municipal', null=True, blank=True )
    numero = models.CharField(max_length=6, help_text='Número do endereço', null=True, blank=True )
    complemento = models.CharField(max_length=40, help_text='Complemento do endereço', null=True, blank=True )
    bairro = models.CharField(max_length=40, help_text='Bairro', null=True, blank=True )
    cidade = models.CharField(max_length=40, help_text='Cidade', null=True, blank=True )
    uf = models.CharField(max_length=2, help_text='UF', null=True, blank=True )
    cep = models.CharField(max_length=7, help_text='CEP', null=True, blank=True )
    telefones = models.CharField(max_length=40, help_text='Telefones', null=True, blank=True )
    email = models.CharField(max_length=100, help_text='Email', null=True, blank=True )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lista_empresas')