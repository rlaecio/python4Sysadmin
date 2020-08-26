#!/usr/bin/env python3

from pymongo import  MongoClient

mongo_con = MongoClient('mongodb://192.168.1.9:27017/')
db = mongo_con["flask-add"]

deleted = db.user.delete_one(
    {
        "name" : "usuario_nome"
    }
    
)

print(deleted.deleted_count)

