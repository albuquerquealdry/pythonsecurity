import random
import string

size = 16

chars = string.ascii_letters + string.digits + '!@#$%¨&*()+-?'

rnd = random.SystemRandom()

password = (''.join(rnd.choice(chars) for i in range(size)))

print (password)