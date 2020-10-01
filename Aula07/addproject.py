#!usr/bin/env python3
import requests
import json

token = "XEQYLB4d-AJgp99QJaSx"


data = {
    "name": "flask-app"
}
projetos = requests.post("http://192.168.1.9/api/v4/projects?private_token={}".format(token), data)
print(projetos.json())
   
