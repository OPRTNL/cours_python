import sqlite3

import sqlite3

connexion = sqlite3.connect("pizzas_1.db")
c = connexion.cursor()

def search_name_in_db(table : str, occurence : str, cursor = c):
    cursor.execute(f'SELECT * FROM {table} where nom = "{occurence}"')
    query = cursor.fetchall()
    if len(query) == 0: return False
    return query

def db_create(table,name,arg, cursor = c):
    cursor.execute(f'INSERT INTO {table} (nom, vegan) VALUES ({name},{arg == 1});')

connexion.commit()
connexion.close()
