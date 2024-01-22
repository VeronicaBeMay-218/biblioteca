# Generated by Django 3.2 on 2024-01-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0008_remove_prestamo_fecha_prestamo'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fecha_devolucio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]