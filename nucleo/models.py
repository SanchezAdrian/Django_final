from django.db import models

# Create your models here.

class Cliente(models.Model):
    Dni=models.CharField(max_length=9,unique=True)
    Nombre=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=70)
    Direccion=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=9)
    FechaNacimiento=models.DateField()

    def __str__(self):
        return self.Dni

    

class Coche(models.Model):
    Marca=models.CharField(max_length=20)
    Modelo=models.CharField(max_length=30)
    Colro=models.CharField(max_length=20)
    FechaMatriculacion=models.DateField()
    Imagen=models.ImageField(upload_to='coches', null=True)
    Cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self):
        return self.Marca




class Mecanico(models.Model):
    Dni=models.CharField(max_length=9,unique=True)
    Nombre=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=70)
    Direccion=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=9)
    FechaNacimiento=models.DateField()

    def __str__(self):
        return self.Dni

class Reparacion(models.Model):
    FechaSolicitud=models.DateField()
    FechaArreglo=models.DateField()
    Motivo=models.CharField(max_length=150)
    Observaciones=models.CharField(max_length=80)
    Arreglado=models.BooleanField(default=False)
    Reparador=models.ForeignKey(Mecanico,on_delete=models.CASCADE)
    Coches=models.ManyToManyField(Coche)
    Clientes=models.ManyToManyField(Cliente)

    def __str__(self):
        return self.Arreglado


class Noticia(models.Model):
    Titulo=models.CharField(max_length=50)
    Texto=models.CharField(max_length=300)
    Foto=models.ImageField(upload_to='noticias')
    FechaCreacion=models.DateField()
    FechaModificacion=models.DateField()
    Creador=models.ForeignKey(Mecanico,on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo