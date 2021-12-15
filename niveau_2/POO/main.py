
## DEFINITION 



class Personne:
    def __init__(self, nom : str, age : int):
        self.nom = nom
        self.age = age

    def Donner_son_nom_et_son_age(self):
        print(f"Bonjour je m'appelle {self.nom} et j'ai {self.age}" + (" ans" if not self.age == 1 else " an") + ".")
        
    def Se_presenter(self):
        print("Bonjour je m'appelle : " + self.nom)

    def is_major(self):
        return self.age >= 18


## UTILISATION

personne_1 = Personne("coucou", 1)
personne_2 = Personne("zob", 23)

personne_1.Se_presenter()
personne_2.Se_presenter()

personne_2.nom = "Champion"

personne_1.Donner_son_nom_et_son_age()
personne_2.Donner_son_nom_et_son_age()

print(personne_1.is_major())
print(personne_2.is_major())
