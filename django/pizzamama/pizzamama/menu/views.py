from cmath import pi
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    pizza_names = [pizza.nom for pizza in pizzas]
    pizza_names_str = ", ".join(pizza_names)
    return HttpResponse("Les pizzas : " + pizza_names_str)