import datetime

from django.db import models

from django.db.models import Q, Count

class LibroManager(models.Manager):
    """managers para el modelo autor"""
    
    def listar_libros(self, kword):#buscador
        resultado= self.filter(
            titulo__icontains=kword,
            fecha__range=('2010-01-01', '2020-01-01')#filtro en base a un rango de fechaas
        )
        return resultado
        
    def listar_libros2(self, kword,fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()#validacion
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()#buscador
        resultado= self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)#filtro en base a un rango de fechaas
        )
        return resultado
        
    def listar_libros_categoria(self, categoria):
    
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
    
    #agregar un nuevo autor a un libro
    def add_autor_libro(self, libro_id, autor): #recuperaar eol libro al cual le vamos a agergar un autor mediante el id
        libro = self.get(id=libro_id)#declaramos variable libro- ghet nos va a recuperar un soolo registro
        #id =_ sl id del libro que nos mandan como parametro
        libro.autores.add(autor) #para agregarloaqui especificamos el autor q queremos agregar
        #autores (manitomany)
        return libro #retorne el mismo libro
    
    def libros_num_prestamos(self):
        resultado=self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado
    
class CategoriaManager(models.Manager): 
#manager era precisamente para aprender a acceder hacia el foreingkey de un manager
#sin necesidad de que este directamente en FK dentro del modelo
    """managers para el modelo Categoria"""
    
    def categoria_por_autor(self, autor):
    
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct() #LAS CONSULTAS NO SE REPITAN
        
        
    #vamos a utilizar un filtro pero usando una funcion especial de django
        #que se llama annotate()
        #dentro de los parentesis. primero voy a declarar una variable 
        #dentro va estra almacenada la operacion aritmeticaque se encarga de contar cuantos elementos tiene esa categoria
        
    def listar_categoria_libros(self):
        resultado=self.annotate(
            num_libros=Count('categoria_libro')#variable= donde va estar almacenaada contar el numero de libros con Cont y que atributo vamos a contar
        )
        for r in resultado:
            print('********')
            print(r, r.num_libros)
        return resultado
    
       
    
    
    
    