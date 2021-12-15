
## DEFINITION 

class Personne:
    def __init__(self, nom):
        self.nom = nom
        
    def Se_presenter(self):
        print("Bonjour je m'appelle : " + self.nom)

## UTILISATION

personne_1 = Personne("coucou")
personne_2 = Personne("zob")

personne_1.Se_presenter()
personne_2.Se_presenter()


