from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibro.as_view(), name="libros"),
    path('libros-2/', views.ListLibro2.as_view(), name="libros2"),
    path('libros-detalle/<pk>', views.LibroDetailView.as_view(), name="libro-detalle"),
    
]