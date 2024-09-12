# Generated by Django 5.1 on 2024-09-07 23:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0002_producto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendedor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.producto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ventas', to='ventas.vendedor')),
            ],
            options={
                'ordering': ['-fecha_venta'],
            },
        ),
    ]
