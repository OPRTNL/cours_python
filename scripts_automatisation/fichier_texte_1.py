import os.path


f = open("mon_premier_fichier.txt", "w")



f.write("bonjour\n")
f.write("SAUCISSON")

f.close()

e = open("mon_premier_fichier.txt", "r")

print(e.read())

e.close()