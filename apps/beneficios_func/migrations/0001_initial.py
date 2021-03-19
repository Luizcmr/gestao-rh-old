# Generated by Django 2.2 on 2020-01-03 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0019_auto_20191216_2149'),
        ('contratos', '0005_contrato_data_inicio_horario'),
        ('beneficios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficios_func',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, help_text='Valor do benefício', max_digits=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'Ativo'), ('I', 'Inativo'), ('S', 'Suspenso'), ('B', 'Bloqueado'), ('C', 'Cancelado'), ('O', 'Outros')], help_text='Status', max_length=1, null=True)),
                ('beneficio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='beneficios.Beneficio')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contratos.Contrato')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario')),
            ],
        ),
    ]