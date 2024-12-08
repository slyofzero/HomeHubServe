from flask import Request, jsonify
from models import execute_query
from werkzeug.security import generate_password_hash, check_password_hash
from utils.auth import create_token

def register_controller(request: Request):
    try:
        body = request.get_json()
        name = body.get("name")
        username = body.get("username")
        password = body.get("password")

        # Check for all fields
        if not name or not username or not password:
            return jsonify({"message": "All fields 'name', 'username' and 'password' are required"}), 400
        
        query = f"SELECT * FROM user WHERE username = '{username}'"
        user = execute_query(query, fetch_one=True)

        # Check if username is unique
        if user is not None:
            return jsonify({"message": "Username already in use"}), 400
        
        encrypted_password = generate_password_hash(password)

        query = f'''
            INSERT INTO user (name, username, password)
            VALUES ('{name}', '{username}', '{encrypted_password}')
        '''
        execute_query(query)

        return jsonify({"message": "User registered successfully"}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500

def login_controller(request: Request):
    try:
        body = request.get_json()
        username = body.get("username")
        password = body.get("password")

        # Check for all fields
        if not username or not password:
            return jsonify({"message": "All fields 'username' and 'password' are required"}), 400
        
        query = f"SELECT * FROM user WHERE username = '{username}'"
        user = execute_query(query, fetch_one=True)

        # Check if username is unique
        if user is None:
            return jsonify({"message": "Invalid username"}), 400

        if not check_password_hash(user["password"], password):
            return jsonify({"message": "Invalid password"}), 401

        token = create_token(user)
        return jsonify({"message": "User logged in successfully", "token": token}), 200
    except RuntimeError as e: 
        return jsonify({"message": str(e)}), 500