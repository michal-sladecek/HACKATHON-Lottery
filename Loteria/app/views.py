"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .forms import BootstrapAuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required



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
            'form' : form,
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
@login_required(redirect_field_name = reverse_lazy('landingPage'))
def home(request):
    return render(request,'home.html')

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
