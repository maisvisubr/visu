from flask import Flask
from blue_prints.video_bp import video_bp
from blue_prints.usuario_bp import usuario_bp

app = Flask(__name__)

app.register_blueprint(video_bp)
app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app.run(debug=True)
