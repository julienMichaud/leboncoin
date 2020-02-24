from rest_framework import routers
from annonces import api_views as annonces_views
#https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/

router = routers.DefaultRouter()
router.register(r'annonces', annonces_views.AnnonceViewSet)
