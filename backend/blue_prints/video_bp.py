from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from pegar_thumb import retorna_thumb

video_bp = Blueprint("video_bp", __name__)

client = MongoClient("mongodb+srv://maisvisubr:sHQu2YbLUGEvgruD@cluster0.um6smo3.mongodb.net/")
db = client["db"]
col_videos = db["videos"]


@video_bp.route("/")
def show_version():
    return jsonify({"version": 1.3})


@video_bp.route("/get_videos", methods=["POST"])
def get_videos():
    return jsonify([v for v in col_videos.find()])


@video_bp.route("/post_videos", methods=["POST"])
def post_videos():
    payload = request.json

    payload.update(
        {
            "thumb": retorna_thumb(payload["url"]),
            "_id": str(ObjectId())
        }
    )

    col_videos.insert_one(
        payload
    )
    
    return jsonify({"msg": "video cadastrado com sucesso"})


@video_bp.route("/update_status_video/<video_id>/<status>", methods=["POST"])
def update_video(video_id, status):
    col_videos.update_one(
        {"_id": video_id},
        {"$set": {"status": status}}  # ATUALIZA O STATUS DO VIDEO (ATIVO, INATIVO)
        # INATIVO PODE SER QUANDO O  VIDEO FOR ASSISTIDO OU USUARIO EXCLUIR O VIDEO

    )
    return jsonify({"msg": "video atualizado com sucesso"})
