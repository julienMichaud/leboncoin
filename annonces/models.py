from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Annonce(models.Model):
    title = models.CharField(max_length=30)
    categoryChoices = (
        ("Cars", "Cars"),
        ("Clothes", "Clothes"),
        ("Manga", "Manga"),
    )
    category = models.CharField(choices=categoryChoices, max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.CharField(max_length=200)
    photo = models.FileField(blank=True,)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")