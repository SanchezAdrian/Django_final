# Generated by Django 3.1.4 on 2021-02-03 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0012_auto_20210203_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparacion',
            old_name='Reparador',
            new_name='Propietario',
        ),
    ]
