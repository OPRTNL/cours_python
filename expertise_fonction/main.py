def afficher_infos_personnes(name, age):
    print(f"Le nom de la personne est {name} son age est {age}")
    name_len = len(name)
    print(f"Le nombre de caractére du prénom est {name_len}")

afficher_infos_personnes("toto", 21)