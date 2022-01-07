import sqlite3
connexion = sqlite3.connect("pizzas_1.db")
c = connexion.cursor()

c.execute("""CREATE TABLE ingredient (
    ingredient_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    nom VARCHAR,
    vegan bool
    );""")

c.execute("""CREATE TABLE pizza (
    pizza_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    nom VARCHAR,
    prix FLOAT,
    ingredient_list_id REFERENCES ingredient_list,
    vegan BOOLEAN
    );""")

c.execute("""CREATE TABLE ingredient_list (
    ingredient_list_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    pizza_id REFERENCES pizza,
    ingredient_id REFERENCES ingredient
    );"""
)

c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Margarita", 8.9, True)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Reine", 7.6, False)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("4 fromages", 10.3, True)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Orientale", 8.9, False)')

pizza_ingredients = ([1, [("Tomates",1),("Mozzarella",1),("Basilic",1)]], [2,[("Tomates",1),("Mozzarella",1),("Jambon",0), ("Champignon",1)]], [3,[("Tomates",1),("Mozzarella",1),("Bleu",1), ("Saint-Nectaire",1), ("Comté",1)]],[4,[("Tomates",1),("Mozzarella",1), ("Merguez",0), ("Basilic",1)]])

def search_name_in_db(table : str, occurence : str, cursor):
    cursor.execute(f'SELECT * FROM {table} where nom = "{occurence}"')
    query = cursor.fetchall()
    if len(query) == 0: return False
    return query

for pizza in pizza_ingredients:
    for i in pizza[1]:
        if not search_name_in_db("ingredient", i[0], c):
            c.execute(f'INSERT INTO ingredient (nom, vegan) VALUES ("{i[0]}",{i[1]});')
        ingredient_index = search_name_in_db("ingredient",i[0],c)
        print(ingredient_index)
        c.execute(f'INSERT INTO ingredient_list (pizza_id,ingredient_id) VALUES ({pizza[0]}, {ingredient_index[0][0]})')


connexion.commit()
connexion.close()

