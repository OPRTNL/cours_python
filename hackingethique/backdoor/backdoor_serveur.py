#SOCKET RESEAU : SERVEUR

import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"en attente d'une connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()
print(f"connexion établie avec {client_adress}")

sent_data = "coucou"
datarecues = "youpi"

while True:
    commande =  input("Commande : ") 
    if commande == "exit":
        break
    elif commande == "":
        continue
    connection_socket.sendall(commande.encode())
    response_bi = connection_socket.recv(MAX_DATA_SIZE)
    if not response_bi:
        break
    response = response_bi.decode()
    print(response)


s.close()
connection_socket.close()

