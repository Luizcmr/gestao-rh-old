from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#from localflavor.br.models import BRCPFField

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from apps.funcoes.models import Funcao

# Criando model funcionario.
class Funcionario(models.Model):

    SN_CHOICES = (
        ('S', u'Sim'),
        ('N', u'Não'),
    )

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
        ('V', u'Outros'),
    )

    nome = models.CharField(max_length=50, help_text="Nome do funcionário")
    #cpf=BRCPFField(max_length=11)
    cpf = models.CharField(max_length=14, help_text="CPF do funcionário", unique=True)
    data_nasc = models.DateField(help_text="Data de Nascimento", null=True, blank=True )
    nacionalidade = models.CharField(max_length=15, help_text="Nacionalidade", null=True, blank=True)
    naturalidade = models.CharField(max_length=25, help_text="Naturalidade", null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
    nome_conjuge = models.CharField(max_length=50, help_text="Nome do Cônjuge", null=True, blank=True )
    nome_pai = models.CharField(max_length=50, help_text="Nome do Pai", null=True, blank=True )
    nome_mae = models.CharField(max_length=50, help_text="Nome da Mãe", null=True, blank=True)
    num_dependentes = models.IntegerField(help_text="Nº Dependentes", null=True, blank=True )
    endereco = models.CharField(max_length=60, help_text='Endereço', null=True, blank=True)
    numero = models.CharField(max_length=6, help_text='Número do endereço', null=True, blank=True)
    complemento = models.CharField(max_length=40, help_text='Complemento do endereço', null=True, blank=True)
    bairro = models.CharField(max_length=40, help_text='Bairro', null=True, blank=True)
    cidade = models.CharField(max_length=40, help_text='Cidade', null=True, blank=True)
    uf = models.CharField(max_length=2, help_text='UF', null=True, blank=True)
    cep = models.CharField(max_length=7, help_text='CEP', null=True, blank=True)
    telefone = models.CharField(max_length=40, help_text='Telefones', null=True, blank=True)
    celular = models.CharField(max_length=40, help_text='Celular', null=True, blank=True)
    email = models.EmailField(max_length=100, help_text='Email', null=True, blank=True)
    rg = models.CharField(max_length=15, help_text="RG do funcionário", null=True, blank=True)
    orgao = models.CharField(max_length=10, help_text="Órgão emissor", null=True, blank=True)
    data_emissao = models.DateField(help_text="Data de emissao", null=True, blank=True)
    cnh = models.CharField(max_length=15, help_text="CNH", null=True, blank=True)
    pis = models.CharField(max_length=15, help_text="Nº do Pis", null=True, blank=True)
    data_pis = models.DateField(help_text="emissao do pis", null=True, blank=True)
    banco_pis = models.CharField(max_length=3, help_text="Banco do pis", null=True, blank=True)
    ag_pis = models.CharField(max_length=3, help_text="Agência do pis", null=True, blank=True)
    ctps = models.CharField(max_length=10, help_text="CTPS", null=True, blank=True )
    ctps_rural = models.CharField(max_length=10, help_text="CTPS Rural", null=True, blank=True)
    titulo = models.CharField(max_length=10, help_text="Título de Eleitor", null=True, blank=True)
    zona = models.CharField(max_length=3, help_text="Zona Eleitoral", null=True, blank=True )
    secao = models.CharField(max_length=3, help_text="Seção Eleitoral", null=True, blank=True )
    cert_militar = models.CharField(max_length=15, help_text="Certificado Militar", null=True, blank=True )
    contato1 = models.CharField(max_length=40, help_text="Primeiro Contato", null=True, blank=True)
    tel_contato1 = models.CharField(max_length=25, help_text="telefone Contato", null=True, blank=True )
    contato2 = models.CharField(max_length=40, help_text="Segundo Contato", null=True, blank=True )
    tel_contato2 = models.CharField(max_length=25, help_text="Telefone Contato", null=True, blank=True )
    cbo = models.CharField(max_length=10, help_text="CBO", null=True, blank=True )
    data_admissao = models.DateField(help_text="Data de Admissão", null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salário", null=True, blank=True)
    estrangeiro = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Estrangeiro(S/N)", null=True, blank=True)
    casado_bras = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Casado com Brasileiro(S/N)", null=True, blank=True)
    tem_filhos_bras = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Filhos com Brasileiro(S/N)", null=True, blank=True)
    qtd_filhos_bras = models.IntegerField(help_text="Quantos Filhos Brasileiros", null=True, blank=True)
    data_chegada = models.DateField(help_text="Data de Chegada Brasil", null=True, blank=True)
    naturalizado = models.CharField(max_length=1, choices=SN_CHOICES, help_text="Naturalizado", null=True, blank=True)
    num_decreto = models.CharField( max_length=10, help_text="Nº Decreto", null=True, blank=True)
    foto = models.ImageField(upload_to='funcionario_foto', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    departamentos = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    data_movto = models.DateField(help_text="Data de Movimentação", null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.cpf = chr_remove(self.cpf, ".-/")

        super(Funcionario, self).save(*args, **kwargs)

    @property
    def mcpf(self):
        return self.cpf[:3] + "." + self.cpf[3:6] + "." + self.cpf[6:9] + "-" + self.cpf[9:11]

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('lista_funcionarios')


def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string