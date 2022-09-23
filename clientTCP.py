import socket

ipServer = 'localhost'
portServer = 12000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect((ipServer,portServer))

msg = input(" Text : ")

clientSocket.send(msg.encode('utf-8'))

print(clientSocket.recv(1024).decode('utf-8'))
clientSocket.send("bye".encode('utf-8'))
print(clientSocket.recv(1024).decode('utf-8'))