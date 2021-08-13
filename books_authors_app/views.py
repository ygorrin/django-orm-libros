from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'libros': Libro.objects.all()
    }
    return render(request, 'index.html', context)

def libros(request):
    context = {
        'libros': Libro.objects.all()
    }
    return render(request, 'libros.html', context)

def autores(request):
    context = {
        'autores': Autor.objects.all()
    }
    return render(request, 'autores.html', context)

def ingresar_libro(request):
    print(request.POST)
    libro = Libro.objects.create(
        titulo = request.POST['titulo'],
        desc = request.POST['desc'],
    )
    return redirect("/libros")


def ingresar_autor(request):
    print(request.POST)
    autor = Autor.objects.create(
        nombre = request.POST['nombre'],
        apellido = request.POST['apellido'],
        notas = request.POST['notas'],
    )
    return redirect("/autores")


def ver_libro(request, id):
    libro = Libro.objects.get(id=id)
    print("-"*10 , "Vamos a mostrar el libro", libro)
    
    autor_add= []
    for author in Autor.objects.all():
        if author not in libro.autores.all():
            autor_add.append(author)

    context = {
        'libro' : libro,
        'autor_add': autor_add,
    }
    return render(request, 'libros_autores.html', context)

def ver_autor(request, id):
    autor = Autor.objects.get(id=id)
    print("-"*10 , "Vamos a mostrar autor: ", autor)
    
    libro_add= []
    for libro in Libro.objects.all():
        if libro not in autor.libros.all():
            libro_add.append(libro)

    context = {
        'autor' : autor,
        'libro_add': libro_add,
    }
    return render(request, 'autor_libros.html', context)


def agregar_autor(request):
    print(request)
    if request.method == 'POST':
        print("---POST ----", request.POST)
        
        libro_id = request.POST["libro_id"]
        autor_id = request.POST["autor_id"]
        print("---POST que llega----", libro_id, autor_id)

        libro = Libro.objects.get(id = libro_id)
        autor = Autor.objects.get(id = autor_id)

        libro.autores.add(autor)
        libro.save()
    return redirect("/ver_libro/"+ libro_id)

def agregar_libro_al_autor(request):
    if request.method == 'POST':
        print("---POST ----", request.POST)
        autor_id = request.POST["autor_id"]
        libro_id = request.POST["libro_id"]

        print("---POST que llega----", libro_id, autor_id)

        libro = Libro.objects.get(id = libro_id)
        autor = Autor.objects.get(id = autor_id)

        autor.libros.add(libro)
        autor.save()
    return redirect("/ver_autor/"+ autor_id)


def eliminar_libro(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('/libros')

def eliminar_autor(request, id):
    autor = Autor.objects.get(id = id)
    autor.delete()
    return redirect('/autores')