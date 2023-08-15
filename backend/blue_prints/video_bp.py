from flask import Blueprint, jsonify
from pymongo import MongoClient

video_bp = Blueprint("video_bp", __name__)

client = MongoClient("mongodb+srv://maisvisubr:sHQu2YbLUGEvgruD@cluster0.um6smo3.mongodb.net/")
db = client["db"]
col_videos = db["videos"]


@video_bp.route("/")
def show_version():
    return jsonify({"version": 1.1})


@video_bp.route("/get_videos", methods=["POST"])
def get_videos():
    return jsonify([v for v in col_videos.find()])
