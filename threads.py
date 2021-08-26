from threading import Thread


def teste1():
    print("Aldrynho")

def teste2():
    print("Albuquerque")


t_carro1 = Thread(target=teste1)
t_carro2 = Thread(target=teste2)

t_carro1.start()
t_carro2.start()