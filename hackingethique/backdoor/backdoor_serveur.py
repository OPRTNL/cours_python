#SOCKET RESEAU : SERVEUR

import socket


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


def socket_receive_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    # print("reception client : ", data_len)
    while current_data_len < data_len:
        chunk = data_len - current_data_len
        if chunk > MAX_DATA_SIZE:
            chunk = MAX_DATA_SIZE

        data = socket_p.recv(chunk)
        # print("Paquet : ", len(data))
        if not data : return None

        if not total_data: 
            total_data = data 
        else: 
            total_data += data

        current_data_len = len(total_data)
        # print(" recu  : ", current_data_len, " / ", data_len)

    return total_data

def send_to_client_and_receive_all_data(connection_socket, commande = 'infos'):
    dl_command = False

    if commande == "exit":
        return False
    elif commande == "":
        return True

    commande_split = commande.split(" ")
    if len(commande_split) > 1 and commande_split[0] == "dl":
        dl_command = True

    connection_socket.sendall(commande.encode())
    header = socket_receive_all_data(connection_socket, 13)
    header_len = int(header)

    response_bi = socket_receive_all_data(connection_socket, header_len)

    if not response_bi:
        return False

    if dl_command:
        if len(response_bi) == 1 and response_bi == b" ":
            response = "Erreur:  Le fichier " + commande_split[1] + " n'existe pas !"
            
        else:
            f = open(commande_split[1],"wb")
            f.write(response_bi)
            f.close()
            response = "Dl ok"
    else:
        response = response_bi.decode()

    return response

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"en attente d'une connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()
print(f"connexion établie avec {client_adress}")

resultat = True

while resultat :
    infos = send_to_client_and_receive_all_data(connection_socket)
    commande = input(client_adress[0] + " : " + str(client_adress[1]) + " " +infos)
    resultat = send_to_client_and_receive_all_data(connection_socket, commande)
    if resultat: print(resultat) 
""""
    commande =  input("Commande : ") 
    if commande == "exit":
        break
    elif commande == "":
        continue
    
    connection_socket.sendall(commande.encode())
    header = socket_receive_all_data(connection_socket, 13)
    header_len = int(header.decode())

    response_bi = socket_receive_all_data(connection_socket, header_len)

    if not response_bi:
        break


    response = response_bi.decode()


    print(response)
"""


s.close()
connection_socket.close()

