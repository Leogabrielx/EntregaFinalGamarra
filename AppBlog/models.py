from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.CASCADE, null=True)
    autor = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, blank=True, null=True)
    texto = RichTextField()
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    