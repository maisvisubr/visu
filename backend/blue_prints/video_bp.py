from flask import Blueprint, jsonify

video_bp = Blueprint("video_bp", __name__)


@video_bp.route("/get_videos", methods=["POST"])
def get_videos():
    return jsonify([])
