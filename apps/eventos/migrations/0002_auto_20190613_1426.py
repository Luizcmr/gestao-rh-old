# Generated by Django 2.2 on 2019-06-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['nome']},
        ),
    ]
