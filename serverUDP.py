import socket

serverPort = 12000
serverIp = 'localhost'

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind((serverIp, serverPort))

print("----------SERVER----------")

while True:
    message1, addressClient = serverSocket.recvfrom(2048)
    messagemodified = message1.upper()

    serverSocket.sendto(messagemodified, addressClient)
