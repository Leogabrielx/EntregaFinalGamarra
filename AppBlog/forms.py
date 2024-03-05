from django import forms
from .models import Categoria, Articulo, Comentario
from django.contrib.auth.models import User

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    
class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['categoria', 'titulo', 'subtitulo', 'texto', 'imagen']
        
    def __init__(self, *args, **kwargs):
        super(ArticuloFormulario, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'