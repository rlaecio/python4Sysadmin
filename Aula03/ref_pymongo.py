#!/usr/bin/env python3

from pymongo import  MongoClient

mongo_con = MongoClient('mongodb://192.168.1.9:27017/')
db = mongo_con["flask-add"]

inserted = db.user.insert_one(
    { 
     'name' : 'usuario_nome', 
     'email' : 'usuario_email', 
     'messages' : [
            {
                'name' : 'usuario_name',
                'message' : 'mensagem'
            }
        ]
    }
) 

print(inserted)