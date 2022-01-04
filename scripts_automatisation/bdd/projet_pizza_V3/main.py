from models import Pizza, PizzaPersonnalisee

pizzas = [Pizza("Margarita", 8.9, ["Tomates","Mozzarella","Basilic"], True), 
          Pizza("Reine", 7.6, ["Tomates","Mozzarella","Jambon", "Champignon"]), 
          Pizza("4 fromages", 10.3, ["Tomates","Mozzarella","Bleu", "Saint-Nectaire", "Comté"], True),
          Pizza("Orientale", 9.9, ["Tomates","Mozzarella", "Merguez", "Basilic"]),
          PizzaPersonnalisee(),
          PizzaPersonnalisee()]


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