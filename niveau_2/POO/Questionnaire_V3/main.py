# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions


def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i+1, "-", choix[i])

    print()
    resultat_response_correcte = False
    reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_response_correcte = True
    else:
        print("Mauvaise réponse")
        
    print()
    return resultat_response_correcte


'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

class Question():
    INDEX = 0
    
    def __init__(self,question : str, reponses : list , bonne_reponse : str):
        self.question = question
        self.reponses = reponses
        self.bonne_reponse = bonne_reponse
        self.numero = Question.INDEX + 1
        Question.INDEX = self.numero
        

    def show_question(self):
        print(self.question + " N° " + str(self.numero))
        nombre = 1
        for i in self.reponses:
            print("  " + str(nombre) + " - " + i)
            nombre += 1

    def demander_la_reponse(self) -> bool:
        min = 1
        max = len(self.reponses)
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return True if self.reponses[reponse_int -1] == self.bonne_reponse else False

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return self.demander_la_reponse()        

class Qcm():
    def __init__(self, questions : list) -> None:
        self.questions = questions
        self.score = 0
        
    def poser_les_questions(self):
        print("--------- Bienvenu dans le questionnaire ! -------------")
        for question in self.questions:
            question.show_question()
            if question.demander_la_reponse():
                self.score += 1
                print(f"Bonne reponse ! Votre score {str(self.score)}")
            else :
                print(f"Mauvaise response ;( Votre score {str(self.score)}")
            

        

questionnaire = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

Qcm1 = Qcm(questionnaire)

Qcm1.poser_les_questions()
