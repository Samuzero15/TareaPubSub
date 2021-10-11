from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30)
    pasw = models.CharField(max_length=16)
    def __str__(self) -> str:
        return self.user

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=1000)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Suscripciones(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
