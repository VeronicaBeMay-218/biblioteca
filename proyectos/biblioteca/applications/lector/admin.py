from django.contrib import admin

# Register your models here.
from .models import Lector
from .models import Prestamo
# Register your models here.

admin.site.register(Lector)
admin.site.register(Prestamo)