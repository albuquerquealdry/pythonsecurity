import os
import pymongo
from pymongo import MongoClient
import datetime

def pingSimple():
    print ("#"*60)

    host = input("enter host: ")
    print ("-"*80)
    os.system('ping -n 10 {}'.format(host))
    print ("-"*80)

    x = datetime.datetime.now()
    def teste():
        client= MongoClient("localhost",27017)
        db = client.mongoDB
        db.data.insert_one({
        "host": host,
        "date": x
        })
    teste()