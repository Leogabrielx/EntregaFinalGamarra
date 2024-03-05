from django.contrib import admin
from .models import Articulo, Categoria, Comentario

# Register your models here.

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'categoria', 'autor')
    list_display = ('titulo', 'categoria', 'autor', 'fecha_publicacion')
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre',)
    
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ('articulo', 'usuario', 'comentario')
    list_display = ('comentario', 'articulo', 'usuario', 'fecha_comentario')