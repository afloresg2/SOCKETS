import socket

ipServer = 'localhost'
portServer = 12000

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind((ipServer,portServer))

serverSocket.listen()

print("Server is ready to receive ")

while True:
    client1, addressClient = serverSocket.accept()

    print(f"Conect to {addressClient}")

    print(client1.recv(1024).decode('utf-8'))

    client1.send("Bye".encode('utf-8'))
    client1.close()