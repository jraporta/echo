# Ayuda de uso de sockets: https://wiki.python.org/moin/HowTo/Sockets

import socket

HOST = '192.168.1.43'
PORT = 4500
print (HOST + ' listening')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea un socket INET de tipo STREAM
server.bind((HOST, PORT)) # asocia el socket a un host público y al puerto definido
server.listen() #convierte el socket en servidor
while True:
    (client, address) = server.accept() # acepta conexiones externas
    print('Connected by', address)
    while True:
        data = client.recv(1024) # escucha el envío del socket cliente
        if not data:
            break
        print (data)
        client.sendall(data) # hace echo
