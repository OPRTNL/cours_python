
#COMPLETION DE LISTES

chauffeurs = ["maxime", "lise", "lucie", "violette"]

distances =[1.2, 0.3, 2.6, 0.1]


chauffeurs_maj = [chauffeur.capitalize() for chauffeur in chauffeurs if chauffeur[0] == "l"]
chauffeurs_maj_si = [chauffeur.capitalize() if chauffeur[0] == "l" else chauffeur for chauffeur in chauffeurs if "s" in chauffeur]
chauffeur_et_dist = [(chauffeurs[i], distances[i]) for i in range(0, len(chauffeurs))]

print(min(chauffeurs[3][0]))
print(chauffeurs)
print(chauffeurs_maj)
print(chauffeurs_maj_si)
print(chauffeur_et_dist)

print(5//2)