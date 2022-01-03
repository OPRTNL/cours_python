import sqlite3

connexion = sqlite3.connect("albums_1.db")

c = connexion.cursor()

c.execute("SELECT * FROM artiste")
artistes = c.fetchall()

print(artistes)

c.close()