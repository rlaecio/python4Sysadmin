#!usr/bin/env python3
import requests
import json

token = "XEQYLB4d-AJgp99QJaSx"


data = {
    "email": "joao.hummel@4linux.com.br",
    "username": "joao.hummel",
    "name": "João Hummel",
    "password": "4linux123"
    
}
usuarios = requests.post("http://192.168.1.9/api/v4/users?private_token={}".format(token), data)
print(usuarios.json())
   
