"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
# Create your models here.

   
class LoteriaModel(models.Model):
    casZrebovania = models.DateTimeField()
    vyzrebovanieCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    zrebovanaSuma = models.IntegerField()

class UserData(models.Model):
    pocetTicketov = models.IntegerField()
    user = models.OneToOneField(User)

class PodanyTicketModel(models.Model):
    casPodania = models.DateTimeField(auto_now_add=True, blank=True)
    loteria = models.ForeignKey(LoteriaModel)
    podaneCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    user = models.ForeignKey(User)