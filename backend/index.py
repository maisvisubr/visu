from flask import Flask
from blue_prints.video_bp import video_bp

app = Flask(__name__)

app.register_blueprint(video_bp)

if __name__ == "__main__":
    app.run()