from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from . models import Autor


class ListAutores(ListView):
    #model = Autor
    context_object_name="lista_autores"
    template_name = "autor/lista.html"
    
    def get_queryset(self):#para usar el manager en buscador
        palabra_clave=self.request.GET.get("kword", '')
        return Autor.objects.buscar_autor4(palabra_clave)

