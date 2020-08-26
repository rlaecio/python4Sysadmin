#!/usr/bin/env python3

from pymongo import  MongoClient

mongo_con = MongoClient('mongodb://192.168.1.9:27017/')
db = mongo_con["flask-add"]

users = db.user.find(
    {
        "name": "usuario_nome",
        "email": "usuario_email"
    } 
)

for user in users:
    print(user)
    print(user["_id"].generation_time)