#!usr/bin/env python3
import requests
import json

token = "XEQYLB4d-AJgp99QJaSx"


usuarios = requests.get("http://192.168.1.9/api/v4/users?private_token={}".format(token))
print(
    json.dumps(
        usuarios.json(),
        indent=4, sort_keys=True
    )
)
