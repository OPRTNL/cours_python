import sqlite3

connexion = sqlite3.connect("pizzas_1.db")
c = connexion.cursor()

c.execute("""CREATE TABLE ingredient (
    ingredient_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    nom VARCHAR
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

#ingredients = ["Tomates","Mozzarella","Basilic","Jambon", "Champignon","Bleu", "Saint-Nectaire", "Comté", "Merguez"]

#for ingredient in ingredients:
#    c.execute(f"""INSERT INTO ingredient (nom) VALUES ("{ingredient}");""")



c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Margarita", 8.9, True)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Reine", 7.6, False)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("4 fromages", 10.3, True)')
c.execute('INSERT INTO pizza (nom, prix, vegan) VALUES ("Orientale", 8.9, False)')

pizza_ingredients = ([1, ["Tomates","Mozzarella","Basilic"]], [2,["Tomates","Mozzarella","Jambon", "Champignon"]], [3,["Tomates","Mozzarella","Bleu", "Saint-Nectaire", "Comté"]],[4,["Tomates","Mozzarella", "Merguez", "Basilic"]])

def search_name_in_db(table : str, occurence : str):
    c.execute(f'SELECT * FROM {table} where nom = "{occurence}"')
    query = c.fetchall()
    print(query)
    if len(query) == 0: return False
    return query

for pizza in pizza_ingredients:
    for i in pizza[1]:
        if not search_name_in_db("ingredient", i):
            c.execute(f'INSERT INTO ingredient (nom) VALUES ("{i}");')
        ingredient_index = search_name_in_db("ingredient",i)
        c.execute(f'INSERT INTO ingredient_list (pizza_id,ingredient_id) VALUES ({pizza[0]}, {ingredient_index[0][0]})')


connexion.commit()
connexion.close()