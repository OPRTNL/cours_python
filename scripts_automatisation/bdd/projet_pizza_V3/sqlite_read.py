import sqlite3

def db_read():
    connexion = sqlite3.connect("pizzas_1.db")

    c = connexion.cursor()

    c.execute("SELECT * FROM pizza")
    pizzas = c.fetchall()

    print(pizzas)
    pizza_args = []

    for pizza in pizzas:
        raw_liste_ingredients = c.execute(f'SELECT ingredient.nom FROM ingredient_list JOIN ingredient ON ingredient_list.ingredient_id = ingredient.ingredient_id WHERE ingredient_list.pizza_id={pizza[0]};')
        liste_ingredient = list(i[0] for i in raw_liste_ingredients)
        liste_pizza = list(pizza)
        liste_pizza[3] = liste_ingredient
        del liste_pizza[0]
        pizza_args.append(liste_pizza)
        
    c.close()
    return pizza_args