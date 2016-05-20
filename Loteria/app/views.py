"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import UserData,NakupnyPlan, LoteriaModel
from datetime import datetime
from .forms import BootstrapAuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

import json
import time

from .konstanty import *
from .loteria import prebiehaLoteria, getCisla, timeToNextLottery, timeOfNextLottery,timeToNextLottery2

def createUserData(user):
    try:
        x = user.userdata
    except ObjectDoesNotExist:
        x = UserData()
        x.user = user
        x.pocetTicketov = 5
        x.save()

def currentLotteryState(request): 
    sprava = []       
    if prebiehaLoteria():
        sprava.append({"prebiehaLoteria": True})
        sprava.append({"zrebovanieZacalo": timeOfNextLottery()})
        sprava.append({"vyzrebovaneCisla": getCisla()})
    else:
        sprava.append({"prebiehaLoteria": False})
        timed = timeToNextLottery()
        s = timed.seconds
        hours, remainder = divmod(s, 3600)
        minutes,seconds = divmod(remainder,60)
        sprava.append({"zrebovanieZacne": timeOfNextLottery()})
        sprava.append({"casDoZrebovania2": timeToNextLottery2()})
        sprava.append({"casDoZrebovania": {"hours":hours, "minutes":minutes, "seconds":seconds }})
    returnVal = json.dumps(sprava)
    return JsonResponse(returnVal,safe=False)

@login_required(login_url = reverse_lazy('landingPage'))
def pocetTiketov(request):
    sprava = []
    user = request.user
    print(UserData.objects.get(user=user).pocetTicketov)
    returnVal = json.dumps([{"pocetTiketov": UserData.objects.get(user=user).pocetTicketov}])
    return JsonResponse(returnVal,safe=False)

def landingPage(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated():
        return home(request)
    form = BootstrapAuthenticationForm()
    return render(
        request,
        'app/index.html',
        {
            'jackpot' : JACKPOT,
            'form' : form,
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
@login_required(login_url = reverse_lazy('landingPage'))
def home(request):
    createUserData(request.user)
    return render(request,'app/home.html')
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
@login_required(login_url = reverse_lazy('landingPage'))
def podajTiket(request): 
    form = TiketForm()
    print(request.POST)
    return render(request, "app/podanieTiketu.html",{'form':form})
def historiaZrebovani(request):
    zrebovania = LoteriaModel.objects.all().order_by('casZrebovania')[:10]
    return render(request,"app/historiaZrebovani.html",{"zrebovania":zrebovania})
# if request.is_ajax():
def kupujem(request):
    if 'id' in request.GET:
       id = request.GET['id']       
       plan = NakupnyPlan.objects.get(pk=id)
       data = UserData.objects.get(user=request.user)
       data.pocetTicketov += plan.pocetTiketov
       data.save()
    return HttpResponseRedirect(reverse_lazy('home'))
def nakupTikety(request):
    plany = NakupnyPlan.objects.all()
    return render(request,'app/buy.html',{
        'plany': plany,
    }
    )