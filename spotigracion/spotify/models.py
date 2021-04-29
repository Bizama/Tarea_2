from django.db import models

# Create your models here.

class Artista(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f'Este artista se llama {self.name} y tiene {self.age} años'

class Album(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    # artist = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return f'Este album llamado {self.name} es del genero: {self.genre}'

class Cancion(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField(null=True)
    times_played = models.IntegerField(null=True)
    # artist = models.ForeignKey(Artista, on_delete=models.CASCADE)
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'Esta cancion se llama {self.name} se ha reproducido {self.times_played} y dura {self.duration}'
