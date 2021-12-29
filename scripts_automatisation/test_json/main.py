import json

f = open("test73.txt", "r")
coucou = f.read()
personnes = json.loads(coucou)
f.close()

print(len(personnes))


class Personne:
    def __init__(self,nom, prenom, email = "", civilite = "M.") -> None:
        self.nom = nom
        self.prenom = prenom
        self.civilite = civilite
        self.email = email

    def FromData(datas):
        p = Personne(datas["LastName"],datas["FirstName"],civilite = datas["Salutation"])
        return p


    def SePresenter(self):
        print("je m'appelle", self.nom, "et mon email est", self.email)

personnes_ob = []

for i in personnes:
    p = Personne.FromData(i)
    personnes_ob.append(p)


for i in personnes_ob:
    i.SePresenter()