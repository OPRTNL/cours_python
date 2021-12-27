alpha_str = "abcdefghijklmnopqrstuvwxyz"

alpha = list(alpha_str)


numbr = []

for i in range(1,27):
    numbr.append(i)


alpha_num = {alpha[i] : numbr[i] for i in range(0,len(numbr))}
num_alpha = {numbr[i] : alpha[i] for i in range(0,len(numbr))}



def get_pwd():
    return input("Mot a encrypter (caractère alphabétiques minuscule uniquement) : ")

def get_key():
    return input("votre clef d'encryption (caractère alphabétiques minuscule uniquement) : ")


def crypto():
    p = get_pwd()
    k = get_key()
    p_list = list(p)
    k_list = list(k)
    k_list_p = []
    index = 0

    for i in range(0,len(p_list)):
        k_list_p.append(k_list[index])
        index += 1
        if index > len(k_list) -1 :
            index = 0

    numbr_p = []

    for i in range(len(p_list)):
        numbr_p.append((alpha_num[p_list[i]] + alpha_num[k_list_p[i]]))
    
    
    index =0
    encrypted_pwd = ""

    for i in numbr_p:
        index = i
        if index > 26:
            index -= 26
        encrypted_pwd += num_alpha[index]
        
    print("Votre cryptage : " , encrypted_pwd)
        


def decrypto():
    # prendre mdp
    a = get_pwd()
    # mdp => liste
    b = get_key()
    # prendre clef => liste
    a_list = list(a)
    # alonger clef de la taille du mdp
    b_list = []
    index = 0
    for i in range(len(a)):
        b_list.append(b[index])
        index += 1
        if index >= len(b) : index = 0

    # soustraire mdp - clef dans une liste avec un dictionnaire lettre valeur
    # boucler sur la liste avec condition < 0 +26
    str_alpha = ""
    numero = 0
    for i in range(len(a_list)):
        numero = alpha_num[a_list[i]] - alpha_num[b_list[i]]
        if numero < 1 : numero += 26
        str_alpha += num_alpha[numero]

    print("Votre decryptage : ",str_alpha)

crypto()
decrypto()
