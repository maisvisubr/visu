from flask import Flask
from flask_cors import CORS
from blue_prints.video_bp import video_bp
from blue_prints.usuario_bp import usuario_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(video_bp)
app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app.run(debug=True)
