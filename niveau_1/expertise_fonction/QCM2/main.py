questions_reponses = []

class Question:
    def __init__(self, question : str, options : list, reponse : str) -> object:
        self.question = question
        self.options = options
        self.reponse = reponse


question_1 = Question("Quelle est la capitale de la France", ["a: Paris", "b: Lyon", "c: Moscou", "d: Londres"], "a")
question_2 = Question("Quelle est la préfecture du Rhône", ["a: Milan", "b: Lyon", "c: Shangai", "d: Limas"], "b")
question_3 = Question("Ou se situe le Kremlin ?", ["a: Saint-Petersbourg", "b: Riga", "c: Moscou", "d: Londres"], "c")
question_4 = Question('Quelle est la ville dont la place financière est appelée la " city " ?', ["a: Milan", "b: Lyon", "c: Moscou", "d: Londres"], "d")

list_of_questions = [question_1,question_2,question_3,question_4]
score = 0

def show_ennonce(question : object):
    print(question.question)
    for i in range(len(question.options)):
        print(question.options[i])


def ask_for_answer():
    answer_good = 0
    while answer_good == 0:
        answer = input("Merci de donner votre réponse en tapant a, b, c ou d : ")
        if answer.lower() in ["a","b","c","d"]:
            answer_good = answer.lower()
        else:
            print("*********** Erreur : votre réponse n'est pas a, b, c ou d *************")

    return answer_good


def is_ok(question : object, answer : str) -> bool:
    return question.reponse == answer


def one_question(question : object):
    global score
    show_ennonce(question)
    answer = ask_for_answer()
    if is_ok(question,answer):
        print("bonne réponse")
        score += 1
    else: 
        print("mauvaise réponse")
        score -= 1


def quizz(questions : list):
    for i in range(len(questions)):
        print("question n°", i + 1, " sur ", len(questions))
        one_question(questions[i])
        print()
    print("Votre score est ", score)

quizz(list_of_questions)