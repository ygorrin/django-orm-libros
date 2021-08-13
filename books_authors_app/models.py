from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #autores 
    def __str__(self):
        return f"Libro: {self.titulo}, {self.desc}"

    def __repr__(self):
        return f"Libro: {self.titulo}, {self.desc}"

class Autor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    libros = models.ManyToManyField(Libro, related_name="autores")
    notas = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Autor: {self.nombre}, {self.apellido}, {self.libros.all()}"

    def __repr__(self):
        return f"Autor: {self.nombre}, {self.apellido}, {self.libros.all()}"
