#libreria 
import socket
#datos necesarios para un socket
ipServer = 'localhost'
portServer = 12000

#instanciamos con el constructor socket 
#1parametro capa 3 ipv4 o ipv6
#2parametro capa 4 Si es UDP o TCP
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#metodo bind 
#1parametro la tupla
serverSocket.bind((ipServer,portServer))

#metodo listen() que indica que esta esperando 
serverSocket.listen()

print("Server is ready to receive ")

while True:
    #metodo funcion accept()
    #nos devuelve cliente, direccion cliente

    client1, addressClient = serverSocket.accept()

    #imprimimos la direccion del cliente
    print(f"Conect to {addressClient}")
    #metodo recv buffer en bytes
    #metodo decode 
    #1parametro tipo de decodificacion
    print(client1.recv(1024).decode('utf-8'))

    #metodo send 
    #1parametro mensaje codificado
    #encode()
    #1parametro tipo de codificacion
    client1.send("Bye".encode('utf-8'))
    #Cerramos el cliente
    client1.close()