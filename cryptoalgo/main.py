alpha_str = "abcdefghijklmnopqrstuvwxyz"

alpha = list(alpha_str)


numbr = []

for i in range(1,27):
    numbr.append(i)


alpha_num = {alpha[i] : numbr[i] for i, v in enumerate(numbr)}
num_alpha = {numbr[i] : alpha[i] for i, v in enumerate(numbr)}



def get_pwd():
    return input("Mot a encrypter (caractère alphabétiques minuscule uniquement) : ")

def get_key():
    return input("votre clef d'encryption (caractère alphabétiques minuscule uniquement) : ")

"""
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

    encrypted_pwd = ""

    for i in range(len(p_list)):
        index = alpha_num[p_list[i]] + alpha_num[k_list_p[i]]
        if index > 26: index -= 26
        encrypted_pwd += num_alpha[index]
        
    print("Votre cryptage : " , encrypted_pwd)
        


def decrypto():
    a = get_pwd()
    b = get_key()
    a_list = list(a)
    b_list = []
    index = 0
    for i in range(len(a)):
        b_list.append(b[index])
        index += 1
        if index >= len(b) : index = 0

    str_alpha = ""
    for i in range(len(a_list)):
        numero = alpha_num[a_list[i]] - alpha_num[b_list[i]]
        if numero < 1 : numero += 26
        str_alpha += num_alpha[numero]

    print("Votre decryptage : ",str_alpha)
"""

def unitcrypto(a_str : str, b_str : str, callback_operator) -> str:
    a_list = list(a_str)
    b_list = []
    index = 0
    for i in enumerate(a_list):
        b_list.append(b_str[index])
        index += 1
        if index >= len(b_str) : index = 0

    str_alpha = ""
    for i, v in enumerate(a_list):
        numero = callback_operator(alpha_num[a_list[i]], alpha_num[b_list[i]])
        if numero > 26 : numero = callback_operator(numero, -26)
        elif numero < 1 : numero = callback_operator(numero, -26)
        str_alpha += num_alpha[numero]
    
    return str_alpha

a = get_pwd()
b = get_key()
print(unitcrypto(a, b, lambda x, y : x + y))
a = get_pwd()
b = get_key()
print(unitcrypto(a, b, lambda x, y : x - y))