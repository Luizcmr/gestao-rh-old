# Generated by Django 2.2 on 2019-12-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_auto_20190514_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='data_entrega',
            field=models.DateField(blank=True, help_text='Data de Entrega', null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='data_vencimento',
            field=models.DateField(blank=True, help_text='Data de Vencimento', null=True),
        ),
    ]
