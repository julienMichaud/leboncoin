from django.urls import path
from .views import (
    AnnonceCreateView,
    OwnAnnonceListView,
    AnnonceUpdateView,
    AnnonceDeleteView,
    AnnonceListView
)

urlpatterns = [
    path('<int:pk>/edit/', AnnonceUpdateView.as_view(), name='annonce_edit'),
    path('<int:pk>/delete/', AnnonceDeleteView.as_view(), name='annonce_delete'),
    path('myannonces/', OwnAnnonceListView.as_view(), name='my_annonces'),
    path('new/', AnnonceCreateView.as_view(), name='annonce_new'),
    path('', AnnonceListView.as_view(), name='annonce_list'),
]