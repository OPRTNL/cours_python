#  demander les variable
nom = input("ton nom  :")
#initialisation varaible age
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
