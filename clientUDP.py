#libreria
import socket
#datos necesarios para crear el socket cliente
serverPort = 12000
serverIp = 'localhost'

#creando socket cliente
#1parametro capa 3 IPv4 o IPv6
#2parametro capa 4 Si es UDP o TCP
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

mssg = input(" TExt: ")

#metodo sendto
#1parametro el mensaje en bytes con encode()
#2parametro tupla IP y Puerto del servidor a quien queremos enviar
clientSocket.sendto(mssg.encode(), (serverIp,serverPort))

#funcion recvfrom 
#1parametro buffer maximo
#devuelve la funcion mensaje y direccion
messagemodified, addressServer = clientSocket.recvfrom(2048)

print("Server Response in UPPERCASE :"+messagemodified.decode())
#cerramos socket cliente
clientSocket.close()