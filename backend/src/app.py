from flask import Flask, Blueprint
from models import db
from config import Config
from routes import auth_bp, user_bp
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

with app.app_context():
    db.init_app(app)
    db.create_all()
    print("Database tables created.")

CORS(app)

api_bp = Blueprint("api", __name__, url_prefix="/api")
api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(user_bp, url_prefix="/user")

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)