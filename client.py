import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('52.79.253.36',12345))
sock.send('hellllllllo'.encode())
data = sock.recv(65535)

print(data.decode())
