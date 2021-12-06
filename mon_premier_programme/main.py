from types import BuiltinMethodType


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
    if age_int == 17:
        print("presque adulte mon jeune")
    elif age_int == 18:
        print("Chapeau tout juste majeur")
    elif age_int < 10:
        print("vous êtes enfant")
    elif age_int > 60:
        print("Vous êtes vieux")
    elif 60 >= age_int > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

 

#  demander la variable nom avec une vrai variable unique
nom_1 = demander_nom()
age_1 = demander_age(nom_1)

#boucle pour demander l'age en testant la validité 
nom_2 = demander_nom()
age_2 = demander_age(nom_2)

show_text(nom_1, age_1)
show_text(nom_2, age_2)
