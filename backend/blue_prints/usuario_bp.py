from flask import Blueprint, request, jsonify
from pymongo import MongoClient

usuario_bp = Blueprint("usuario_bp", __name__)
client = MongoClient("mongodb+srv://maisvisubr:sHQu2YbLUGEvgruD@cluster0.um6smo3.mongodb.net/")
db = client["db"]
col_usuarios = db["usuarios"]


@usuario_bp.route("/cadastrar", methods=["POST"])
def cadastrar_usuario():
    if not col_usuarios.find_one({"login": request.json["login"]}):
        payload = request.json
        payload.update({"_id": request.json["login"]})
        col_usuarios.insert_one(
            payload  # APENAS INSERE OS DADOS NO BD
        )
        return jsonify(
            {
                "msg": "Usuário criado com sucesso!",
                "success": True
            }
        )
    else:
        return jsonify(
            {
                "msg": "Usuário já existe!",
                "success": False
            }
        )


@usuario_bp.route("/logar", methods=["POST"])
def logar_usuario():
    payload = request.json  # DADOS QUE TU VAI ME PASSAR
    login = payload["login"]
    senha = payload["senha"]

    if not (usuario := col_usuarios.find_one({"login": login})):  # VERIFICO SE TEM O USUÁRIO NO BD
        return jsonify(
            {
                "msg": "Usuário não encontrado!",
                "success": False
            }
        )

    if usuario["senha"] != senha:  # VERIFICO A SENHA NO BD
        return jsonify(
            {
                "msg": "Senha incorreta!",
                "success": False
            }
        )

    return jsonify(
        {
            "msg": usuario["_id"],
            "success": True
        }
    )  # RETORNO O ID QUE TEM QUE SER SALVO NO CACHE DO NAVEGADOR


@usuario_bp.route("/<_id>/moedas")  
def atualizar_moeda(_id):

    moedas = col_usuarios.find_one({"_id": _id}).get("moedas")

    return jsonify({"msg": moedas})
