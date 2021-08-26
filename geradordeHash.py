import hashlib

print("-"*60)

entrada = input("Digite o seu texto: \n")
print("-"*60)
resultado = hashlib.md5(entrada.encode('utf-8'))

print (resultado.hexdigest())