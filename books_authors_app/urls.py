from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    path('libros', views.libros),
    path('ingresar_libro', views.ingresar_libro),
    path('ver_libro/<int:id>', views.ver_libro),
    path('agregar_autor', views.agregar_autor),
    path('eliminar_libro/<int:id>', views.eliminar_libro),


    path('autores', views.autores),
    path('ingresar_autor', views.ingresar_autor),
    path('ver_autor/<int:id>', views.ver_autor),
    path('agregar_libro_al_autor', views.agregar_libro_al_autor),
    path('eliminar_autor/<int:id>', views.eliminar_autor),

]
