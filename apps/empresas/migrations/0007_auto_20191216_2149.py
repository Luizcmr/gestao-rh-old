# Generated by Django 2.2 on 2019-12-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_auto_20190613_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cep',
            field=models.CharField(blank=True, help_text='CEP', max_length=8, null=True),
        ),
    ]
