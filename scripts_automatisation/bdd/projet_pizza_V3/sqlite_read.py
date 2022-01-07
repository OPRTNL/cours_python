import sqlite3

def search_name_in_db(table : str, occurence : str, cursor):
    cursor.execute(f'SELECT * FROM {table} where nom = "{occurence}"')
    query = cursor.fetchall()
    if len(query) == 0: return False
    return query

def db_read():
    connexion = sqlite3.connect("pizzas_1.db")

    c = connexion.cursor()

    c.execute("SELECT * FROM pizza")
    pizzas = c.fetchall()
    pizza_args = []

    for pizza in pizzas:
        raw_liste_ingredients = c.execute(f'SELECT ingredient.ingredient_id, ingredient.nom, ingredient.vegan FROM ingredient_list JOIN ingredient ON ingredient_list.ingredient_id = ingredient.ingredient_id WHERE ingredient_list.pizza_id={pizza[0]};')
        liste_ingredient = list(i for i in raw_liste_ingredients)
        liste_pizza = list(pizza)
        liste_pizza[3] = liste_ingredient
        pizza_args.append(liste_pizza)
    
    c.close()
    return pizza_args
