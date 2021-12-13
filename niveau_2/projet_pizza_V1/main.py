pizzas = ["4 fromages", "calzone", "reine", "jambon fromage"]


def show_menu(dishes, nb = -1):
    c = dishes if nb == -1 else dishes[0:nb]
    if len(c) == 0 : 
        print("Aucune pizza")
        return
    print(f"******** Liste des pizzas ({len(c)}) ********")
    c.sort()
    for i in c : print(i)

def show_first_last(dishes):
    if len(dishes) == 0 : 
        print("Aucune pizza")
        return
    print(f"Première pizza {dishes[0]}")
    print(f"Dernière pizza {dishes[-1]}")

def add_dish(dishes):
    new_dish = input("Souhaitez vous ajouter une Pizzas ?")
    if new_dish.lower() in dishes:
        print("Cette pizza existe déjà")
    else:
        dishes.append(new_dish)


show_menu(pizzas, 2)
show_first_last(pizzas)
add_dish(pizzas)
show_menu(pizzas)
show_first_last(pizzas)