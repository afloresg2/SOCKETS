import socket

serverPort = 12000
serverIp = 'localhost'

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

mssg = input(" TExt: ")

clientSocket.sendto(mssg.encode(), (serverIp,serverPort))

messagemodified, addressServer = clientSocket.recvfrom(2048)
print("Server Response in UPPERCASE :"+messagemodified.decode())
clientSocket.close()