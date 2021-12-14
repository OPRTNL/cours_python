# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"


fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))


definir_les_extensions = {i[0]:i[1] for i in definition_extensions}


def trouver_extension(element):
    #itérer sur la liste pour trouver l'index du point
    decompose = element.split(".")
    if len(decompose) > 1:
        return decompose[-1].lower()
    
    return False


for nom in fichiers:
    try :
        print(nom, f"({definir_les_extensions[trouver_extension(nom)]})")
    except :
        print(nom, "(Aucune Extension)") if not trouver_extension(nom) else print(nom, "(Extension non-reconnue)")




'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''



# lower/upper 
# in / index / for
# split
# -1

# extraire extension



# faire la correspondance définition

