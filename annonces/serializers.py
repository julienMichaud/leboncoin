from .models import Annonce
from rest_framework import serializers

class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = ['title', 'category', 'price', 'description', 'photo', 'author']
