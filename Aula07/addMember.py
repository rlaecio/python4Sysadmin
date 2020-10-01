#!usr/bin/env python3
import requests
import json

token = "XEQYLB4d-AJgp99QJaSx"

project_id = 4
data = {
    "user_id": 3,
    "access_level": 40
}
projetos = requests.post("http://192.168.1.9/api/v4/projects/{}/members?private_token={}".format(project_id, token), data)
print(projetos.json())
   
