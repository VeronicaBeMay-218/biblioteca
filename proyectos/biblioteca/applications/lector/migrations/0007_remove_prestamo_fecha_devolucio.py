# Generated by Django 3.2 on 2024-01-22 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0006_rename_fecha_devolucion_prestamo_fecha_devolucio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='fecha_devolucio',
        ),
    ]
