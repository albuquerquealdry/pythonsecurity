import os
import datetime
from pymongo import MongoClient
import datetime

def pingMultiplo():
        print("#"*60)

        host1= input("Enter Host: ")
        host2= input("Enter Host: ")
        host3= input("Enter Host: ")
        host4= input("Enter Host: ")
        host5= input("Enter Host: ")
        date= datetime
        def pingtest ():
            os.system('ping -n 3 {}'.format(host1))
            os.system('ping -n 3 {}'.format(host2))
            os.system('ping -n 3 {}'.format(host3))
            os.system('ping -n 3 {}'.format(host4))
            os.system('ping -n 3 {}'.format(host5))
            print (date)    
        pingtest()
        x = datetime.datetime.now()

        def mongoInsert():
            client= MongoClient("localhost",27017)
            db = client.mongoDB
            db.data.insert_one({
            "host1": host1,
            "host2": host2,
            "host3": host3,
            "host4": host4,
            "host5": host5,
            "date": x
            })

        mongoInsert ()