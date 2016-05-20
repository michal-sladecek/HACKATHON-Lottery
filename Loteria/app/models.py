"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TicketModel(models.Model):
    casZrebovania = models.DateTimeField()
    vyzrebovanieCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    zrebovanaSuma = models.IntegerField()

class UserData(models.Model):
    pocetTicketov = models.IntegerField()
    user = models.OneToOneField(User)

class PodanyTicketModel(models.Model):
    podaneCisla = models.CharField(max_length=50,validators=[int_list_validator()])
    user = models.ForeignKey(User)