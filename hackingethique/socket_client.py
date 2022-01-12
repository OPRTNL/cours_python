from mmap import MADV_DONTNEED
import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"connexion au serveur {HOST_IP} sur le port {HOST_PORT}")

while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : Impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print("connecté au serveur")
        break

datarecues = s.recv(MAX_DATA_SIZE)
print(datarecues.decode())


s.close()