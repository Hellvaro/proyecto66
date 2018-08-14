from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


# Create your models here.
class Instrumento (models.Model):
    nombreInstrumento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreInstrumento

class Comuna(models.Model):
        nombreComuna = models.CharField(max_length=100)

        def __str__(self):
            return self.nombreComuna

class Estilo(models.Model):
        nombreEstilo = models.CharField(max_length=100)

        def __str__(self):
            return self.nombreEstilo

class Tipo_Local(models.Model):
        nombreTipoLocal = models.CharField(max_length= 100)

        def __str__(self):
            return self.nombreTipoLocal


class Musico (models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    instrumento = models.ManyToManyField(Instrumento)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estilo = models.ManyToManyField(Estilo)
    imagenMusico = models.ImageField(upload_to= 'musicos',null=True, blank=True, width_field="width_field",
                                    height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    nombreMusico = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    expFormacion = models.TextField(max_length=450)
    dispEnsayo = models.TextField(max_length=200)
    dispConciertos = models.TextField(max_length=200)
    dispInmediata = models.BooleanField(None)
    equipado = models.BooleanField(None)
    descripcionEquipo = models.TextField(max_length=450, blank=True)
    contacto = models.CharField(max_length=200)
    aniosExperiencia = models.IntegerField()
    descripcionPersonal = models.TextField(max_length=400, blank= True)
    videoMusico = EmbedVideoField()
    buscaBanda = models.BooleanField(None)
    influencias = models.TextField(max_length=400)
    clasesParticulares = models.BooleanField(None)
    musicoCreacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    beneficio1 = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreMusico
    class Meta:
        ordering = ['-musicoCreacion']

class Banda (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    estilo = models.ManyToManyField(Estilo)
    imagenBanda = models.ImageField(upload_to='bandas' ,null = True,blank=True, width_field="width_field" ,height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    musicos = models.ManyToManyField(Instrumento,blank=True)
    nombreBanda = models.CharField(max_length= 100)
    descripcionBanda = models.TextField(max_length= 400)
    miembros = models.TextField(max_length=100)
    anioFormacion = models.IntegerField()
    historia = models.TextField(max_length=700)
    discografia = models.TextField(max_length=650)
    videoBanda = EmbedVideoField()
    contacto = models.CharField(max_length=200)
    bandaCreacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    beneficio1= models.BooleanField(default=False)

    def __str__(self):
        return self.nombreBanda

    class Meta:
        ordering = ['-bandaCreacion']

class Local (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tipo_Local = models.ForeignKey(Tipo_Local, on_delete=models.CASCADE)
    imagenLocal = models.ImageField(upload_to= 'locales', blank=True, width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombreLocal = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=700)
    buscaBanda = models.BooleanField(False)
    buscaMusico = models.BooleanField(False)
    contacto = models.CharField(max_length=200)
    horarios = models.TextField(max_length=200, default='')
    localCreacion = models.DateTimeField(auto_now= False, auto_now_add=True)#revisar
    beneficio1 = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreLocal





