from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=18, help_text='CNPJ da empresa', unique=True)
    fantasia = models.CharField(max_length=40, help_text='Nome fantasia', null=True, blank=True )
    endereco = models.CharField(max_length=60, help_text='Endereço', null=True, blank=True )
    insc_est = models.CharField(max_length=20, help_text='Inscrição Estadual', null=True, blank=True )
    insc_mun = models.CharField(max_length=20, help_text='Inscrição Municipal', null=True, blank=True )
    numero = models.CharField(max_length=6, help_text='Número do endereço', null=True, blank=True )
    complemento = models.CharField(max_length=40, help_text='Complemento do endereço', null=True, blank=True )
    bairro = models.CharField(max_length=40, help_text='Bairro', null=True, blank=True )
    cidade = models.CharField(max_length=40, help_text='Cidade', null=True, blank=True )
    uf = models.CharField(max_length=2, help_text='UF', null=True, blank=True )
    cep = models.CharField(max_length=8, help_text='CEP', null=True, blank=True )
    telefones = models.CharField(max_length=40, help_text='Telefones', null=True, blank=True )
    email = models.CharField(max_length=100, help_text='Email', null=True, blank=True )

    class Meta:
        ordering = ['nome']

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.cnpj = chr_remove(self.cnpj, ".-/")
        super(Empresa, self).save(*args, **kwargs)

    @property
    def mcnpj(self):
        return self.cnpj[:2] + "." + self.cnpj[2:5] + "." + self.cnpj[5:8] + "/" + self.cnpj[8:12] + "-" + self.cnpj[12:14]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lista_empresas')

def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string