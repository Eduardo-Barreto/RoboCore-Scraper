from flask import Flask
from history.routes import history_bp
from ranking.routes import ranking_bp
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
app.json.ensure_ascii = False
app.json.sort_keys = False

app.register_blueprint(history_bp, url_prefix="/history")
app.register_blueprint(ranking_bp, url_prefix="/ranking")

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
