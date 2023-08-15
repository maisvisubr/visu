from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

usuario_bp = Blueprint("usuario_bp", __name__)
client = MongoClient("mongodb+srv://maisvisubr:sHQu2YbLUGEvgruD@cluster0.um6smo3.mongodb.net/")
db = client["db"]
col_usuarios = db["usuarios"]


@usuario_bp.route("/cadastrar")
def cadastrar_usuario():
    col_usuarios.insert_one(
        request.json.update({"_id": str(ObjectId())})  # APENAS INSERE OS DADOS NO BD
    )
    return jsonify({"msg": "Usuário criado com sucesso!"})


@usuario_bp.route("/logar")
def logar_usuario():
    payload = request.json  # DADOS QUE TU VAI ME PASSAR
    login = payload["login"]
    senha = payload["senha"]

    if not (usuario := col_usuarios.find_one({"login": login})):  # VERIFICO SE TEM O USUÁRIO NO BD
        return jsonify({"msg": "Usuário não encontrado!"})

    if usuario["senha"] != senha:  # VERIFICO A SENHA NO BD
        return jsonify({"msg": "Senha incorreta!"})

    return jsonify({"msg": usuario["_id"]})  # RETORNO O ID QUE TEM QUE SER SALVO NO CACHE DO NAVEGADOR


@usuario_bp.route("/atualizar_moedas/<usuario_id>/<qtd_moedas>")  # O _ID TEM QUE PEGAR DO CACHE E MANDAR NO PATH DA REQUISIÇÃO
def atualizar_moeda(usuario_id, qtd_moedas):
    col_usuarios.update_one(
        {"_id": usuario_id},  # PEGA O ID DO USUARIO SALVO NO CACHE DO NAVEGADOR
        {"$set": {"moedas": qtd_moedas}}  # ATUALIZA AS MOEDAS NO BD
    )
    return jsonify({"msg": "qtd_moedas atualizada do usuario"})
