import requests
import json


data = {
    "nome" : "joao",
    "sobrenome" : "hummel"
}

requisicao = requests.delete(
    "http://httpbin.org/delete",
    json=data 
)

json_to_dict = requisicao.json()
print( json_to_dict )
