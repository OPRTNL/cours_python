def demander_age(nom_du_gars):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_du_gars + " quel est ton age ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR : l'age n'est pas un nombre")
    return age_int


def demander_nom():
    nom_str = input("ton nom  :")
    while nom_str == "":
        print("le nom saisi est une valeur vide")
        nom_str = input("ton nom  :")
    return nom_str

def show_text(nom_str, age_int):
    print("Tu t'appelle " + nom_str + " et ton age est " + str(age_int) + " ans.")
    print("L'année prochaine tu aura " + str(age_int+1))

#  demander la variable nom avec une vrai variable unique
nom = demander_nom()

#boucle pour demander l'age en testant la validité 
age = demander_age(nom)

show_text(nom, age)