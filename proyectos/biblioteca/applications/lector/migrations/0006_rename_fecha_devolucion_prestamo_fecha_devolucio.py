# Generated by Django 3.2 on 2024-01-22 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0005_auto_20240122_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='fecha_devolucion',
            new_name='fecha_devolucio',
        ),
    ]