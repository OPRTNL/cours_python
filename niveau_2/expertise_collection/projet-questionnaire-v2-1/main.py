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

def ask_for_choice(list):
    rep = input(f"Votre réponse (choisissez un nombre entre 1 et {len(list)}) :")

    try:
        r = int(rep)
        if r in range(0,len(list)):
            return r     
        else:
            print (f"merci de saisir un nombre entre 1 et {len(list)}")
            ask_for_choice(list)
    except :
        print(f"Merci de rentrer un nombre entre 1 et {len(list)}")
        ask_for_choice(list)


def poser_question(question):
    global score
    ennonce_question = question[0]
    reponses = question[1]
    reponse_ok = question[2]
    print("QUESTION")
    print("  " + ennonce_question)
    for i in range(len(reponses)):
        print(f"{i + 1} - ",reponses[i])
        print()
    reponse_int = ask_for_choice(reponses)
    if reponse_int - 1 == reponses.index(reponse_ok):
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
