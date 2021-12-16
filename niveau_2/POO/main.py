
## DEFINITION 



class Personne:
    def __init__(self, nom : str = "", age : int = 0) :
        self.nom = nom
        if nom == "":
            self.ask_for_name()
        
        self.age = age

    def Donner_son_nom_et_son_age(self):
        donner_son_nom = f"Bonjour je m'appele {self.nom}"
        donner_son_age =  f" et j'ai {self.age}" + (" ans" if not self.age == 1 else " an") + "."
        print(donner_son_nom + donner_son_age if self.age != 0 else donner_son_nom)
        print("Je suis majeur" if self.is_major() else "Je suis mineur")

    def is_major(self) -> bool:
        return self.age >= 18

    def ask_for_name(self) -> str:
        self.nom = input("Choisissez un nom pour votre Personne : ")


## UTILISATION

personne_1 = Personne(age = 18)
personne_2 = Personne("zob", 23)

personne_1.Donner_son_nom_et_son_age()
personne_2.Donner_son_nom_et_son_age()