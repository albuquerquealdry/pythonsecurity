import ipaddress

ip = '8.8.8.8'

endereco = ipaddress.ip_address(ip)

print (endereco + 100)