from flask import Flask
from models import db
from config import Config
from routes import auth_bp
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI

with app.app_context():
    db.init_app(app)
    db.create_all()
    print("Database tables created.")

CORS(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)