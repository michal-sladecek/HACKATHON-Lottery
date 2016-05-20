"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
# Create your models here.

   
class LoteriaModel(models.Model):
    casZrebovania = models.DateTimeField(auto_now_add=True)
    vyzrebovaneCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    zrebovanaSuma = models.IntegerField()

    def __str__(self):
        return str(self.casZrebovania)


class UserData(models.Model):
    pocetTicketov = models.IntegerField()
    user = models.OneToOneField(User)

class PodanyTicketModel(models.Model):
    casPodania = models.DateTimeField(auto_now_add=True, blank=True)
    loteria = models.ForeignKey(LoteriaModel)
    podaneCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    user = models.ForeignKey(User)

class NakupnyPlan(models.Model):
    cena = models.DecimalField(max_digits=10,decimal_places=2)
    pocetTiketov = models.IntegerField()
    text = models.CharField(max_length=200)