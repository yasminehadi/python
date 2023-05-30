#serveur UDP (CTRL+F2 pour stopper)
import socket

UDP_IP_DU_BINOME = "172.18.51.131"   #adresse de mon serveur
UDP_PORT_DU_BINOME = 5000        #port de mon serveur

# Crée un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))

boucle=True
while(boucle):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data=None
            continue
        print ('received ', data)
        if (data.decode()=='q'):
            boucle=False
print('closing socket')
sock.close()