from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from . models import Libro


class ListLibro(ListView):
    #model = Autor
    context_object_name="lista_libros"
    template_name = "libro/lista.html"
    
    def get_queryset(self):#para usar el manager en buscador
        palabra_clave=self.request.GET.get("kword", '')
        f1=self.request.GET.get("fecha1", '')
        f2=self.request.GET.get("fecha2", '')
        
        if f1 and f2:
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)#crear el manager para el listar libro


class ListLibro2(ListView):
    #model = Autor
    context_object_name="lista_libros"
    template_name = "libro/lista2.html"
    
    def get_queryset(self):#para usar el manager en buscador
        return Libro.objects.listar_libros_categoria('4')#manager que se creo
        

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"
