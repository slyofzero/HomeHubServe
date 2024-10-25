from flask import Flask
from models import init_db
from routes import auth_bp

app = Flask(__name__)

# Initialize the database
init_db(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)
