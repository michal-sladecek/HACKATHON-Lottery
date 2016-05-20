from .models import LoteriaModel
from .konstanty import *
import threading
from random import choice
from datetime import *
import time
vyzrebovaneCisla = []
beziLoteria=False
dalsiaLoteria = datetime.now()
novaLoteria = LoteriaModel()
def loteria():
    return novaLoteria
def getCisla():
    return vyzrebovaneCisla

def timeOfNextLottery():
    epoch = datetime.utcfromtimestamp(0)
    return (dalsiaLoteria - epoch).total_seconds() * 1000.0

def timeToNextLottery2():
    epoch = datetime.utcfromtimestamp(0)
    return (dalsiaLoteria - datetime.now()).total_seconds() * 1000.0

def timeToNextLottery():
    if beziLoteria==True:
        return 0
    return dalsiaLoteria-datetime.now()
    
def prebiehaLoteria():
    return beziLoteria
    
def vytvorLoteriu(suma):
    global novaLoteria
    global vyzrebovaneCisla
    global beziLoteria
    vyzrebovaneCisla = []
    nevyzrebovaneCisla = [x for x in range(MIN_CISLO_NA_TIKETE,MAX_CISLO_NA_TIKETE+1)]
    beziLoteria = True
    for x in range(POCET_CISEL_NA_TIKETE):
        time.sleep(WAIT_TIME_FOR_NUMBER)
        zrebujCislo(nevyzrebovaneCisla)
    novaLoteria.vyzrebovaneCisla = ','.join(map(str, vyzrebovaneCisla))
    novaLoteria.save()
    time.sleep(2)
    global dalsiaLoteria
    dalsiaLoteria = dalsiaLoteria+timedelta(minutes=WAIT_TIME_FOR_LOTTERY)
    beziLoteria = False
    novaLoteria = LoteriaModel()
    novaLoteria.save()

def zrebujCislo(nevyzrebovaneCisla):
    cislo = choice(nevyzrebovaneCisla)
    vyzrebovaneCisla.append(cislo)
    nevyzrebovaneCisla.remove(cislo)

def mam_zrebovat():
    while True:
        if datetime.now() > dalsiaLoteria and not beziLoteria:
            vytvorLoteriu(JACKPOT)     

def startup():
    t1 = threading.Thread(target=mam_zrebovat)
    t1.start()
    print("Startup was succesful")
    