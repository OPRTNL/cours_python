nom_chauffeurs = ["Patrick","Paul","Marc", "Jean", "pierre", "Marie", "Maxime"]
distance_chauffeur_kilometre = [1.5, 2.2, 0.4,0.9,7.1,1.1,0.6]

distance_min = distance_chauffeur_kilometre[0]

i = 0
index_ok = 0

while True:
    if distance_min > distance_chauffeur_kilometre[i] :
        distance_min = distance_chauffeur_kilometre[i]
        index_ok = i
    elif i == len(distance_chauffeur_kilometre) - 1:
        break
    i += 1

print(f"distance minimale {distance_min} km")
print(f"Votre chauffeur est {nom_chauffeurs[index_ok]}")