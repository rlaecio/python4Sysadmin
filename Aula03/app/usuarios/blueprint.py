from flask import Blueprint, Response, request
from config import mongo_db
from bson.json_util import dumps

usuarios_routes = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)

@usuarios_routes.route("")
def getUsuarios():
    try:
        users = mongo_db.user.find()
        return Response(dumps(users), status=200, content_type="application/json")
    except Exception as e:
        return "Erro: {}".format(e)

@usuarios_routes.route("", methods=["POST"])
def postUsuarios():
    try:
        user  = request.get_json()
        mongo_db.user.insert_one(
            {
                "name": user["name"],
                "email": user["email"],
                "messages": []
            }
        )
        response = {"message": "Usuario '{}' criado com sucesso!".format( user["name"] )} 
        return Response(dumps(response), status=201, content_type="application/json")
    except Exception as e:
        return "Erro: {}".format(e)

@usuarios_routes.route("", methods=["PATCH"])
def patchUsuarios():
    try:
        user = request.get_json()
        update = mongo_db.user.update_one(
            { "email": user["email"] },
            { "$set": user}
        )
        
        if update.modified_count:
            response = { "message": "Usuário '{}' atualizado com sucesso!".format(user["name"]) }
            return Response(dumps(response), status=200, content_type="applicatio/json")
        
        elif update.matched_count:
            response = { "message": "Usuário '{}' encontrado, mas não foi modificado!".format(user["name"]) }
            return Response(dumps(response), status=400, content_type="applicatio/json")
        
        else:
            response = { "message": "Usuário '{}' não foi encontrado!".format(user["name"]) }
            return Response(dumps(users), status=404, content_type="applicatio/json")
        
    except Exception as e:
        return "Erro: {}".format(e)
 

@usuarios_routes.route("", methods=["DELETE"])
def deleteUsuarios():
    try:
        user = request.get_json()
        deleted = mongo_db.user.delete_one(
            { "email": user["email"] },
        )
        
        if deleted.deleted_count:
            response = { "message": "Usuário '{}' removido com sucesso!".format(user["email"]) }
            return Response(dumps(response), status=200, content_type="applicatio/json")
        
        else:
            response = { "message": "Usuário '{}' não foi encontrado!".format(user["email"]) }
            return Response(dumps(users), status=404, content_type="applicatio/json")
        
    except Exception as e:
        return "Erro: {}".format(e)
    