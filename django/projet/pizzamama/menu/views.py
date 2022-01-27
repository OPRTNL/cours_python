from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    '''
    pizzas = Pizza.objects.all()
    pizzas_name_price = [f"{pizza.nom} : {pizza.prix}€ " for pizza in pizzas]
    pizzas_str = ", ".join(pizzas_name_price)
    return HttpResponse("Les pizzas : " + pizzas_str)
    '''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html',{'pizzas':pizzas})

def cool(request):
    return HttpResponse("ouais")