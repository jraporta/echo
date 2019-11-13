import socket

HOST = '192.168.1.43'
PORT = 4500

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
client.send(bytes(input(),'utf-8'))
data = client.recv(1024)

print('Received', str(data))
