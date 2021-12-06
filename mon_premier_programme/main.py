#  demander la variable nom avec une vrai variable unique
nom = input("ton nom  :")
while nom == "":
    print("le nom saisi est une valeur vide")
    nom = input("ton nom  :")

#initialisation varaible
age = 0

#boucle pour demander l'age en testant la validité 
while age == 0:
    age_str = input("ton age ")
    try:
        age = int(age_str)
    except:
        print("ERREUR : l'age n'est pas un nombre")

print("Tu t'appelle " + nom + " et ton age est " + str(age) + " ans.")
print("L'année prochaine tu aura " + str(age+1))
