alpha_str = "abcdefghijklmnopqrstuvwxyz"

alpha = list(alpha_str)

print(alpha)

numbr = []

for i in range(1,27):
    numbr.append(i)

print(numbr)

alpha_num = {alpha[i] : numbr[i] for i in range(0,len(numbr))}
num_alpha = {numbr[i] : alpha[i] for i in range(0,len(numbr))}


print(alpha_num)

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
        


crypto()
