# Generated by Django 3.1.4 on 2021-02-08 14:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0016_auto_20210208_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='Texto',
            field=ckeditor.fields.RichTextField(max_length=300),
        ),
    ]
