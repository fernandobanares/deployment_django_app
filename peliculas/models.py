from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    horario = models.DateTimeField()

    def __str__(self):
        return self.titulo
