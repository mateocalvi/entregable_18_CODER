from django.shortcuts import render
from datetime import datetime

from Autos.models import Familiar

# Create your views here.

def index(request): 
    return render(request, "Autos/index.html")

def familiar(request, name:str="name", years:int=0, birth:str='1900-12-31'): # , nacimiento:str='1900-12-31'
    familiar =Familiar(name=name, years=years, birth=birth)
    familiar.save()
    
    context_dict = {
        'familiar': familiar,
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="Autos/familiar.html"
        )