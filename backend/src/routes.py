from flask import request, jsonify
from models import get_db

def init_routes(app):

    @app.route('/services', methods=['GET'])
    def get_services():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM service')
        services = cursor.fetchall()
        return jsonify(services)

    @app.route('/service', methods=['POST'])
    def create_service():
        data = request.json
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO service (name, price, description) VALUES (?, ?, ?)',
            (name, price, description)
        )
        db.commit()
        return jsonify({"message": "Service created!"}), 201
