class Pizza:
    TYPE_DE_PLAT = "PIZZA"
    INDEX = 0

    def __init__(self, index, nom : str,prix : float ,ingredients : list = [], vegan : bool = False):
        self.nom =nom
        self.prix = prix
        self.ingredients = ingredients #== [] : self.DemanderIngredients()  jv;b
        self.vegan = vegan
        self.index = index
        Pizza.INDEX = self.index
    
    def From_Data(list : list):
        print(list[3])
        i = (Ingredient.From_Data(i) for i in list[3])
        p = Pizza(list[0],list[1],list[2],i, list[4]==1)
        return p

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

    def __init__(self):
        super().__init__(Pizza.INDEX,"Personnalisee", 0, [])
        self.index = Pizza.INDEX + 1
        Pizza.INDEX = self.index
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

class Ingredient:
    INDEX = 0

    def __init__(self, index : int, nom : str, vegan : bool):
        self.index = index
        Ingredient.INDEX = self.index
        self.nom = nom
        self.vegan = vegan

    def From_Data(list : list):
        i = Ingredient(list[0],list[1],list[2]==1)
        return i