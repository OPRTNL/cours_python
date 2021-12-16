# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool = None):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        if not genre == None:
            self.genre = genre 
        else: 
            self.demander_le_sexe()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        print(self.dire_le_genre())
        e_optionnel = "" if self.genre else "e"
        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)
        print()

        print()

    def dire_le_genre(self):
        dire_le_genre =  "Genre : Masculin" if self.genre else "Genre : Feminin"
        return dire_le_genre

    def demander_le_sexe(self):
        choix = input('Quel est le sexe de la personne ? Tapez 1 pour Homme et 2 pour Femme : ')
        if choix != "1" and choix != "2":
            print("Erreur : Vous devez saisir 1 ou 2")
            return self.demander_le_sexe()

        self.genre = choix == "1"

         
    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie", 17)
personne2.SePresenter()