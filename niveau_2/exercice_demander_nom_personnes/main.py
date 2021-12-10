def demander_nom(index) -> str:
    nom = input(f"nom de la personne {index}")
    return nom


def programme_demander_nom(list : list) -> list: 
    index = 1
    nom = demander_nom(index)
    while not nom == "":
        list.append(nom)
        index += 1
        nom = demander_nom(index)

name_list = []

programme_demander_nom(name_list)

for i in name_list : print(i)

        
