from django import forms
from django.forms import widgets
from .models import Categoria, Noticia

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre'
        ]

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo', 'cuerpo', 'id_categoria'
        ]

