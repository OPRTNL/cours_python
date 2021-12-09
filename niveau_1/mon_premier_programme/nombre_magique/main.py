import random

NB_MIN = 1
NB_MAX = 10
NB_MAGIQUE = random.randint(NB_MIN,NB_MAX)
NB_VIE = 3

#dire bonjour
# demander valeur à l'utilisateur
def ask_nb():
    number = 0
    while number == 0:
        nb = input(f"Choisissez un chiffre entre {NB_MIN} et {NB_MAX}: ")
        try :
            number = int(nb)
        except :
            print("ERREUR : Vous devez demander un nombre")
        else:
            if NB_MIN > number or number > NB_MAX:
                print(f"Le nombre n'est pas compris entre {NB_MIN} et {NB_MAX} : réessayez")
                number = 0
    return number

# tester si valeur correspond nb Magique
def test_if_ok(nb):
    ok = False
    if nb == NB_MAGIQUE:
        print("******************** Bravo vous avez gagné ********************")
        ok = True
    elif nb < NB_MAGIQUE : print("Plus grand !")
    elif nb > NB_MAGIQUE : print("Plus petit")
    return ok

# caller en nombre de vie
def execute(life):
    for i in range(0,life):
        value_test = False
        print(f"vous avez {life} vie")
        nombre = int(ask_nb())
        value_test = test_if_ok(nombre)
        life -= 1
        if value_test == True : break
        elif life == 0 : print(f"******************** vous n'avez plus de vie perdu ! : le nombre magique était {NB_MAGIQUE} ********************")


execute(NB_VIE)