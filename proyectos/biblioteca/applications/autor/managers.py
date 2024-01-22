from django.db import models

from django.db.models import Q
class AutorManager(models.Manager):
    """managers para el modelo autor"""
    
    def buscar_autor(self, kword):#buscador
        resultado= self.filter(
            nombre__icontains=kword#busca con almenos una letra
        
        )
        return resultado
    
    #busca en tanto en nombre como en apellidos
    def buscar_autor2(self, kword):
        resultado= self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        
        )
        return resultado

    #quiero que me busque en base al nombre o me filte en base al nombre segun li que estoy enviando desde olacasilla de texto
    def buscar_autor3(self, kword):#buscador
    
        resultado= self.filter(
            nombre__icontains=kword
            #busca con almenos una letr
        ).exclude(
            Q(edad__icontains=34) | Q(edad__icontains=63) #no muestra los quetengan la edad de 34 y 63
        )
        return resultado
    
    #quiero q me lieste autores cuya edad sea mayor que
    def buscar_autor4(self, kword):#buscador
        resultado= self.filter(
            edad__gt=34, # MAYOR QUE coma para el Y
            edad__lt=63 #MENOR QUE
        ).order_by('apellidos', 'nombre', 'id')
        
        return resultado