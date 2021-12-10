nom_chauffeurs = ["Patrick","Paul","Marc", "Jean", "pierre", "Marie", "Maxime"]
distance_chauffeur_kilometre = [1.5, 2.2, 0.4,0.9,7.1,1.1,0.6]

distance_min = distance_chauffeur_kilometre[0]

for distance in distance_chauffeur_kilometre:
    if distance < distance_min:
        distance_min = distance

sorted_chauffeurs = distance_chauffeur_kilometre.sort()

index = distance_chauffeur_kilometre.index(distance_min)

print(f"distance minimale {distance_min} km")
print(f"Votre chauffeur est {nom_chauffeurs[index]}")