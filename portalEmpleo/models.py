from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Razón social')
    nit =  models.IntegerField(default=0)
    descripcion = models.TextField(blank=True,help_text='Breve descripción de su empresa')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Oferta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    salario =  models.IntegerField(default=0)
    habiliadades = models.CharField(max_length=100)
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Postulacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fecha_nacimiento =models.DateField(verbose_name='Fecha de nacimiento',null=True,blank=True)
    profesion=models.CharField(verbose_name='Profesión',max_length=30,null=True,blank=True)
    descripcion_perfil = models.TextField(blank=True, verbose_name='Descripción del perfil')
    numero_identificacion = models.IntegerField(default=0, verbose_name='Numero de identificación')
    celular =  models.IntegerField(default=0)