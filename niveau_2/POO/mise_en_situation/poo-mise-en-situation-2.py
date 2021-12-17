# POO EXERCICE DE MISE EN SITUATION 2
class Personne:
    def __init__(self, nom: str, age : int = -1):
        self.nom = nom   # crée une variable d'instance : nom
        if not age == -1:
            self.age = age
        else :
            self.demander_age()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

    def demander_age(self):
        age_dder = input("Quel age à votre personne ? : ")
        self.age = int(age_dder)

personne1 = Personne("Jean")
personne1.SePresenter()

personne2 = Personne("Emilie")
personne2.SePresenter()