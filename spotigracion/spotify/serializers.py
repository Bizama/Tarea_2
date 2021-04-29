from rest_framework import serializers 
from .models import Album, Artista, Cancion

class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Artista
        fields = ('name', 'age')