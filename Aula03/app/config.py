from pymongo import MongoClient

mongo_con = MongoClient('mongodb://192.168.1.9:27017/')
mongo_db = mongo_con["flask-add"]
