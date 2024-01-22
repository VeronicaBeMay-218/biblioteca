from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Categoria
from .models import Libro
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Libro)