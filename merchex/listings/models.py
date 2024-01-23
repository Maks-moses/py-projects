from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    def __str__(self) -> str:
        return f'{self.nom}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RYTHM_AND_BLUES = 'RB'
        SOUL = 'S'
        JAZZ = 'J'
        RUMBA = 'R'
        SALSA = 'SA'
    
    class Type_annoucement(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'Clothes'
        POSTERS = 'Posters'
        MISCELLANEOUS = 'Miscellaneous'

    nom = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    annee_de_creation = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    page_officielle = models.fields.URLField(null=True, blank=True)
    type = models.fields.CharField(choices=Type_annoucement.choices, max_length=20)
    description  = models.fields.CharField(blank = True, max_length=1000)
    


class Title(models.Model):
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Type_annoucement(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'Clothes'
        POSTERS = 'Posters'
        MISCELLANEOUS = 'Miscellaneous'
    
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) #params : Band est le modele auquel on veut se rattacher ; 
                                                                         # null=True parce que nous voulons la creation de l'annonce meme si elles ne sont directements liees a un groupe ; 
                                                                         # on_delete=models.SET_NULL c'est ici que nous decidons de la strategie a suivre lorsque les objects Band sont supprimes. 
     
    title = models.CharField(max_length=100)
    description = models.fields.CharField(max_length=800)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(choices=Type_annoucement.choices, max_length=20)
    
