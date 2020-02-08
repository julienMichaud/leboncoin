from .models import Annonce
import django_filters

class AnnonceFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Annonce
        fields = ['category']
