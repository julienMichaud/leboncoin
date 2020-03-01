from rest_framework import viewsets, generics
from .serializers import AnnonceSerializer
from .models import Annonce
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated

#https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/
# https://www.django-rest-framework.org/api-guide/filtering/
class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    filterset_fields = ['category', 'price', 'author']


class MyAnnonceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AnnonceSerializer
    filterset_fields = ['category', 'price']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Annonce.objects.filter(author=user)


