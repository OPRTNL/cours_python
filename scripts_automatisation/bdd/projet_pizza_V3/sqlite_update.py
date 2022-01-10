import sqlite3


def db_create(table,name,arg):
    connexion = sqlite3.connect("pizzas_1.db")
    c = connexion.cursor()
    c.execute(f'INSERT INTO {table} (nom, vegan) VALUES ("{name}",{arg});')
    connexion.commit()
    connexion.close()


