
def est_majeur(age):
    return "Majeure" if age >= 18 else "Mineure"

def afficher_infos_personne(name, age):
    print(f"Le nom de la personne est {name} son age est {age}")
    name_len = len(name)
    print(f"Le nombre de caractére du prénom est {name_len}")
    print(f"La personne est {est_majeur(int(age))}")

def recuperer_infos_personne(index):
    name = input(f"Nom de la personne {index} : ")
    age = int(input(f"Age de la personne {index} : "))
    return [name, age]

def recuperer_et_afficher_nom_personne(index):
    nom_et_age_list = recuperer_infos_personne(index)
    afficher_infos_personne(nom_et_age_list[0], nom_et_age_list[1])

nb_de_personnes = 3

for i in range(nb_de_personnes) : recuperer_et_afficher_nom_personne(i + 1)