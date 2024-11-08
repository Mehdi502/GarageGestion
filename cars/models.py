from django.db import models

# Create your models here.

class Car(models.Model):
    immatriculation = models.CharField(max_length=15, primary_key=True)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    etat = models.CharField(max_length=20)


