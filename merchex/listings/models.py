from turtle import title
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        COMPAS='CP'
        RABODAY='RBD'
        HIP_HOP='HH'
    name = models.fields.CharField(max_length=255)
    genre=models.fields.CharField(choices=Genre.choices,max_length=6)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    title=models.fields.CharField(max_length=100, blank=True)
    band=models.ForeignKey(Band,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'