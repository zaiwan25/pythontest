import socket
from datetime import datetime

server_addr = ('localhost', 6789)
max_size = 1000

print('Starting the client at ', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()