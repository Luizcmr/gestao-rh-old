# Generated by Django 2.2 on 2019-06-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcoes', '0003_funcao_salario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcao',
            options={'ordering': ['nome']},
        ),
    ]
