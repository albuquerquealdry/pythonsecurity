import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ('Client Socket Create')

host = 'localhost'
port = 5433
mensage = ' Test server'

try:
    print('Client'+ mensage)
    s.sendto(mensage.encode(), (host, 5432))

    data, servidor = s.recvfrom(4096)
    data = data.decode()
    print("Client:" + data)
finally:
    print('Cliente: Fechando a conexão')
    s.close()


