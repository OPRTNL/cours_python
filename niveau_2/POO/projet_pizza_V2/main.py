class Pizza:
    TYPE_DE_PLAT = "PIZZA"

    def __init__(self, nom : str,prix : float ,ingredients : list = [], vegan : bool = False):
        self.nom =nom
        self.prix = prix
        self.ingredients = ingredients #== [] : self.DemanderIngredients()
        self.vegan = vegan

    def ShowPizz(self):
        vegetarienne = (" - " + self.EstVegetarienne()) if self.vegan else ""
        print(self.TYPE_DE_PLAT + " " + self.nom + " : " + str(self.prix) + " €"+ vegetarienne)
        print(", ".join(self.ingredients))
        print("")

    def EstVegetarienne(self):
        if self.vegan :
            return "VEGETARIENNE"
        else :
            return "NON-VEGETARIENNE"

class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENTS = 1.2
    INDEX = 0

    def __init__(self):
        super().__init__("Personnalisee", 0, [])
        self.index = self.INDEX + 1
        PizzaPersonnalisee.INDEX = self.index
        self.nom = self.nom + " " + str(self.index)
        self.demander_ingredient_utilisateur()
        self.calculer_le_prix()

    def demander_ingredient_utilisateur(self):
        print("")
        print(f"Ingredients pour la pizza personnalisée {str(self.index)}")
        ingredient = input("Ajouter un nouvel ingrédient (Enter pour terminer) :")
        if not ingredient == "":
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s) à votre pizza : {', '.join(self.ingredients)}")
            return self.demander_ingredient_utilisateur()

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + (len(self.ingredients)*self.PRIX_PAR_INGREDIENTS)

pizzas = [Pizza("Margarita", 8.9, ["Tomates","Mozzarella","Basilic"], True), 
          Pizza("Reine", 7.6, ["Tomates","Mozzarella","Jambon", "Champignon"]), 
          Pizza("4 fromages", 10.3, ["Tomates","Mozzarella","Bleu", "Saint-Nectaire", "Comté"], True),
          Pizza("Orientale", 9.9, ["Tomates","Mozzarella", "Merguez", "Basilic"]),
          PizzaPersonnalisee(),
          PizzaPersonnalisee()]


print("")
print("------------ LISTE DES PIZZAS ------------")
print("")
for pizza in pizzas:
    pizza.ShowPizz()
    print("")

print(str(PizzaPersonnalisee.INDEX))


"""
print("")
print("------------ LISTE DES PIZZAS Filtrée ------------")
print("")

def tri(e):
    return len(e.ingredients)

pizzas.sort(key=tri)


for pizza in pizzas :
    pizza.ShowPizz()
    """