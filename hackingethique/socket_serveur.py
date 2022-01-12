#SOCKET RESEAU : SERVEUR

import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"en attente d'une connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()

texte_envoye =  "bonjour"
connection_socket.sendall(texte_envoye.encode())

print(f"connexion établie avec {client_adress}")

