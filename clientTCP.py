#libreria
import socket

#datos necesarios para conectarnos al servidor
ipServer = 'localhost'
portServer = 12000

#instanciamos el socket cliente con el constructor socket
#1 parametro capa 3 ipv4 o ipv6
#2 parametro capa 4 si es UDP o TCP
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#metodo connect() para conectarse al servidor
#1parametro la tupla del servidor
clientSocket.connect((ipServer,portServer))

msg = input(" Text : ")

#enviamos mensaje al servidor
clientSocket.send(msg.encode('utf-8'))

#recibimos respuesta del servidor
#metodo recv buffer max
#decode para decodificar
print(clientSocket.recv(1024).decode('utf-8'))
#enviamos al servidor con send()
#1parametro mensaje codificado

clientSocket.send("bye".encode('utf-8'))

print(clientSocket.recv(1024).decode('utf-8'))