from .models import LoteriaModel
from .konstanty import *
import threading
from random import choice
from datetime import *
import time
vyzrebovaneCisla = []
nevyzrebovaneCisla = []
beziLoteria=False
dalsialoteria = time.time()

def getCisla():
    return vyzrebovaneCisla

def timeToNextLottery():
    if beziLoteria==True:
        return 0
    return dalsiaLoteria-time.time()
    
    
def vytvorLoteriu(suma):
    print("ZREBUJEM")
    novaLoteria = LoteriaModel()
    novaLoteria.zrebovanaSuma = suma
    nevyzrebovaneCisla = [x for x in range(MIN_CISLO_NA_TIKETE,MAX_CISLO_NA_TIKETE+1)]
    beziLoteria = True
    for x in range(POCET_CISEL_NA_TIKETE):
        time.sleep(WAIT_TIME_FOR_NUMBER)
        zrebujCislo()
    novaLoteria.vyzrebovaneCisla = ','.join(map(str, vyzrebovaneCisla))
    novaLoteria.save()
    dalsiaLoteria = dalsiaLoteria+timedelta(minutes=WAIT_TIME_FOR_LOTTERY)
    beziLoteria = False

def zrebujCislo():
    cislo = choice(nevyzrebovaneCisla)
    vyzrebovaneCisla.append(cislo)
    nevyzrebovaneCisla.remove(cislo)

def mam_zrebovat():
    print("MAM ZREBOVAT?")
    if time.time() > dalsialoteria and not beziLoteria:
        vytvorLoteriu(JACKPOT)     

def startup():
    print("AAAAAAAAAA")
    t1 = threading.Thread(target=mam_zrebovat)
    t1.start()
    