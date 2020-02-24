from rest_framework import viewsets
from .serializers import AnnonceSerializer
from .models import Annonce
#https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/
class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer