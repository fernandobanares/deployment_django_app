from django.shortcuts import render
from .models import Pelicula

def mostrar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'mostrar_peliculas.html', {'peliculas': peliculas})
