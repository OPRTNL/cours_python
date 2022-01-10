from models import Ingredient, Pizza, PizzaPersonnalisee
from sqlite_read import db_read


pizza_list = db_read()
pizzas =[]

for i in pizza_list:
    pizzas.append(Pizza.From_Data(i))
print(len(Ingredient.OCCCURENCE_LIST))

pizzas += (PizzaPersonnalisee(),PizzaPersonnalisee())

print(len(Ingredient.OCCCURENCE_LIST))

print("")
print("------------ LISTE DES PIZZAS ------------")
print("")
for pizza in pizzas:
    pizza.ShowPizz()
    print("")


"""
print("")
print("------------ LISTE DES PIZZAS Filtrée ------------")
print("")

def tri(e):
    return len(e.ingredients)

pizzas.sort(key=tri)


for pizza in pizzas :
    pizza.ShowPizz()
    """
