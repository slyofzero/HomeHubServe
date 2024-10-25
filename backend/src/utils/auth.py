import jwt
import datetime
from config import Config

def create_token(username: str):
    payload = {
        "username": username,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(days=30)
    }

    token = jwt.encode(payload, Config.JWT_SECRET)
    return token

def decode_token(token):
    try:
        decoded_token = jwt.decode(token, Config.JWT_SECRET)
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}, 401
