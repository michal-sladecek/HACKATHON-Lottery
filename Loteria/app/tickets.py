from datetime import datetime
from django.contrib.auth.models import User
from .models import PodanyTicketModel
from .konstanty import *

def podajTicket(cisla, user):
    if not isinstance(user,User):
        return False
    if not isinstance(cisla, list):
        return False
    if len(cisla) != POCET_CISEL_NA_TIKETE:
        return False
    for x in cisla:
        if x<MIN_CISLO_NA_TIKETE or x>MAX_CISLO_NA_TIKETE:
            return False
    if mozePodatTiket(user):
        p = PodanyTicketModel(user=user)
        p.podaneCisla = ','.join(map(str, cisla)) 
        p.loteria = dalsiaLoteria
        p.save()

def mozePodatTiket(user):
    