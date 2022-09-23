#libreria
import socket
#datos necesario para levantar el servidor
serverPort = 12000
serverIp = 'localhost'

#creando socket servidor
#1parametro capa 3 IPv4 o IPv6
#2parametro capa 4 Si es UDP o TCP
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#metodo 
#1parametro tupla (ip,puerto)
serverSocket.bind((serverIp, serverPort))

print("----------SERVER----------")

#Modo LIstening 
while True:
    #metodo funcion recvfrom()
    #1parametro buffer max
    #funcion devuelve nos da el, mensaje y la direccionCliente
    message1, addressClient = serverSocket.recvfrom(2048)

    #  PROCESO

    # PROCESO
    #modifico a mayusculas
    messagemodified = message1.upper()
    #metodo sendto
    #1parametro "loqueQuierasEnviar"
    #2parametro direccion a la que envias
    serverSocket.sendto(messagemodified, addressClient)
