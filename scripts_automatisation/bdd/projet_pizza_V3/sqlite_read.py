import sqlite3

def db_read():
    connexion = sqlite3.connect("pizzas_1.db")

    c = connexion.cursor()

    c.execute("SELECT * FROM pizza")
    pizzas = c.fetchall()

    print(pizzas)

    for pizza in pizzas:
        liste_ingredient = c.execute(f'SELECT * FROM ingredient_list AS list JOIN ingredient AS ing ON list.ingredient_id = ing.ingredient_id ingredient WHERE pizza_id = {pizza[0]};').fetchall
        print(liste_ingredient)

    c.close()

db_read()