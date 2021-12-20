class Pizza:
    TYPE_DE_PLAT = "PIZZA"

    def __init__(self, nom : str,prix : float ,ingredients : list, vegan : bool = False):
        self.nom =nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegan = vegan

    def ShowPizz(self):
        vegetarienne = (" - " + self.Est_Vegetarienne()) if self.vegan else ""
        print(self.TYPE_DE_PLAT + " " + self.nom + " : " + str(self.prix) + " €"+ vegetarienne)
        print(", ".join(self.ingredients))

    def EstVegetarienne(self):
        if self.vegan :
            return "VEGETARIENNE"
        else :
            return "NON-VEGETARIENNE"



pizza1 = Pizza("Saucisse", 8.9, ["Tomates","Fromage","Saucisse"], True)

pizza1.ShowPizz()