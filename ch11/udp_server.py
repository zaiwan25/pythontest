from datetime import datetime
import socket

server_addr = ('localhost', 6789)
max_size = 4096

print('Starting server', datetime.now())
print('Waiting for a client to call')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_addr)

data, client = server.recvfrom(max_size)

print('At', datetime.now(), client, 'said', data)
server.sendto(b'Are you talking about to me?', client)
server.close()
6