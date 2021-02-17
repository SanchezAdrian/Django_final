# Generated by Django 3.1.4 on 2021-01-20 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dni', models.CharField(max_length=9, unique=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=70)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=9)),
                ('FechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=20)),
                ('Modelo', models.CharField(max_length=30)),
                ('Colro', models.CharField(max_length=20)),
                ('FechaMatriculacion', models.DateField()),
                ('Imagen', models.ImageField(null=True, upload_to='coches')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dni', models.CharField(max_length=9, unique=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=70)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=9)),
                ('FechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaSolicitud', models.DateField()),
                ('FechaArreglo', models.DateField()),
                ('Motivo', models.CharField(max_length=150)),
                ('Observaciones', models.CharField(max_length=80)),
                ('Arreglado', models.BooleanField(default=False)),
                ('Clientes', models.ManyToManyField(to='nucleo.Cliente')),
                ('Coches', models.ManyToManyField(to='nucleo.Coche')),
                ('Reparador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('Texto', models.CharField(max_length=300)),
                ('Foto', models.ImageField(upload_to='noticias')),
                ('FechaCreacion', models.DateField()),
                ('FechaModificacion', models.DateField()),
                ('Creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.mecanico')),
            ],
        ),
    ]