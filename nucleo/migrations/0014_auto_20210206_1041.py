# Generated by Django 3.1.4 on 2021-02-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0013_auto_20210203_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='FechaModificacion',
            field=models.DateField(null=True),
        ),
    ]
