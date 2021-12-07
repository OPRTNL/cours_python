# dire bonjour
print("Bienvenu dans le QCM")
# Demander le nom
#nom = input("Quel est votre prénom jeune personne ?")
nom = "culcul"
# Print bonjour
print(f"Bonjour {nom}, nous allons vous poser des questions ?")
# Définir les réponses possibles
answer_a =  "le lion"
answer_b =  "le tigre"
answer_c =  "le zèbre"
answer_d =  "le loup"
answer_list = [answer_a, answer_b, answer_c, answer_d]

# Print les questions
question_a = "Qui est le roi de la jungle ?"

# Print les différentes solutions
def print_answer_list(answer_list):
    for i in range(0, len(answer_list)):
        print(i+1, answer_list[i])

# Prompt la réponse
def ask_answer(list_of_possibilities):
    user_answer = 0
    while not user_answer in range(1, len(list_of_possibilities) + 1):
        print_answer_list(list_of_possibilities)
        try: 
            user_answer_str = input("Répondez en saisissant le numéro de la réponse")
            user_answer = int(user_answer_str)
            if not user_answer in range(1, len(list_of_possibilities) + 1):
                print("le numéro de votre réponse ne correspond pas aux solutions proposées")
        except:
            print("votre réponse n'es pas valide")
    return user_answer


# Afficher la bonne réponse
def ask_question(question, list_of_questions, right_answer):
    user_answer = 0
    while not user_answer == right_answer:
        print(question)
        user_answer = ask_answer(list_of_questions)
        if user_answer == right_answer:
            print("bravo c'est la bonne réponse")
        else:
            print("mauvaise réponse merci de recommencer")

ask_question(question_a, answer_list, 1)