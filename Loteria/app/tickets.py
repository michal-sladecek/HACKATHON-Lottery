from datetime import datetime
from django.contrib.auth.models import User
from .models import PodanyTicketModel, UserData
from .konstanty import *

def podajTicket(cisla, user):
    print(cisla)
    if not isinstance(user,User):
        print("1")
        return False
    if not isinstance(cisla, list):
        print("2")
        return False
    if len(cisla) != POCET_CISEL_NA_TIKETE:
        print("3")
        return False
    for x in cisla:
        if x<MIN_CISLO_NA_TIKETE or x>MAX_CISLO_NA_TIKETE:
            print("3")
            return False
    if mozePodatTiket(user):
        p = PodanyTicketModel(user=user)
        p.podaneCisla = ','.join(map(str, cisla)) 
        from .loteria import loteria
        loteria().save()
        p.loteria = loteria()
        p.save()
        q = UserData.objects.get(user=user)
        q.pocetTicketov -= 1
        q.save()
        return True
    return False

def mozePodatTiket(user):
    data = UserData.objects.get(user=user)
    if data.pocetTicketov > 0:
        return True
    return False
    