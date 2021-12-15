# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Nombre total de caractères"

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

"""
# 1 for et len
nb_caractere = 0
for nom in noms: nb_caractere += len(nom) 

print(nb_caractere)

# 2 sum
noms_len = sum([len(nom) for nom in noms])
"""

#3 join et len

noms_len = len("".join(noms))


print(noms_len) 

coucou = [1,2,3,4,5]

print(coucou[1:3])

