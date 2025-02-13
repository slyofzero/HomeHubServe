import jwt
import datetime
from config import Config
from models import User

def create_token(user: User):
    payload = {
        "email": user.email,
        "role": user.role,
        "iat": datetime.datetime.now().timestamp(),
        "exp": (datetime.datetime.now() + datetime.timedelta(days=30)).timestamp()
    }

    token = jwt.encode(payload, Config.JWT_SECRET, algorithm="HS256")
    return token

def decode_token(token):
    try:
        decoded_token = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        return decoded_token, True
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}, False
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}, False