#!/usr/bin/env python3

from pymongo import  MongoClient

mongo_con = MongoClient('mongodb://192.168.1.9:27017/')
db = mongo_con["flask-add"]

users = db.user.update_one(
    {
        "name": "usuario_nome",
        "email": "usuario_email"
    },
    {
        "$set": {
            'email': 'usuario@email.pt'
        }
    } 
)

print(users.matched_count, users.modified_count)