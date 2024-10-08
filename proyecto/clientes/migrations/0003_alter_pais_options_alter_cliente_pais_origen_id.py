# Generated by Django 5.1 on 2024-09-04 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_pais_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pais de origen', 'verbose_name_plural': 'Paises de origen'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.pais', verbose_name='Pais de origen'),
        ),
    ]
