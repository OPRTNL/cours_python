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

ingredients = ["Tomates","Mozzarella","Basilic","Jambon", "Champignon","Bleu", "Saint-Nectaire", "Comté", "Merguez"]

for ingredient in ingredients:
    c.execute(f"""INSERT INTO ingredient (nom) VALUES ("{ingredient}");""")

#mj_id = c.lastrowid
#c.execute("""INSERT INTO artiste (nom) VALUES ("Celine Dion");""")
#cd_id = c.lastrowid
#c.execute(f'INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({mj_id}, "Thriller", 1983);')
#c.execute(f'INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({cd_id}, "2X", 1992);')
#c.execute(f'INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({cd_id}, "Let\'s talk about love", 1997);')

connexion.commit()
connexion.close()