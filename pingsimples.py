import os

print ("#"*60)

host = input("Enter host or ip: ")
print ("-"*80)
os.system('ping -n 10 {}'.format(host))
print ("-"*80)
