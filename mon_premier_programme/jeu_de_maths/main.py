import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 3

def ask_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0,1)
    
    result = a + b if o == 1 else a * b
    operator = "+" if o == 1 else "*"
        
    answer_int = 0

    while answer_int == 0:
        answer_str = input(f"Quel est le résultat de {a} {operator} {b} ?")
        try:
            answer_int = int(answer_str)
        except:
            print("ERREUR : La réponse n'est pas un nombre !")
    if answer_int == result:
        print("Bonne réponse")
        return True
    else: 
        print("Faux la réponse était", result)
        return False

def questions():
    question = NB_QUESTIONS
    score = 0
    while not question == 0:
        print(f"question {NB_QUESTIONS - question + 1} sur {NB_QUESTIONS}")
        reponse = ask_question()
        if reponse == True : score += 1
        question -= 1
    
    print(f"Test terminé ! Votre score est de {score}/{NB_QUESTIONS}")
    return score

def appreciation():
    mean = NB_QUESTIONS/2
    score = questions()
    score_float = float(score)
    if score_float >= mean:
        print("Excellent") if score == NB_QUESTIONS else print("Pas Mal!")
    else :
        print("Révisez vos maths") if score == 0 else print("Peut mieux faire")

appreciation()