from os import error
import socket
import sys
import datetime
from pymongo import MongoClient

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
def main ():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou") 
        print ("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")


host = input ("Enter to Host or Ip request connect: ")
port = int(input("Enter endport request connect: "))

try:
    s.connect((host, port))
    print ("Cliet connect for sucesseful")
    s.shutdown(2)
except socket.error as e:
    print("Error Connect")
    sys.exit()

if __name__ == "__main__":
    main()

    x = datetime.datetime.now()
    def teste():
        client= MongoClient("localhost",27017)
        db = client.mongoDB
        db.data.insert_one({
        "host": host,
        "port": port,
        "hour": x
        })
    teste()