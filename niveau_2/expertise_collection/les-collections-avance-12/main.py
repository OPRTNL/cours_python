# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Nombre total de caractères"

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

#
nb_caractere = 0
for nom in noms: nb_caractere += len(nom) 

print(nb_caractere)