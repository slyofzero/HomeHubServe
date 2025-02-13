from werkzeug.security import generate_password_hash
from models import db, User
import re

def is_valid_email(email: str) -> bool:
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def create_admin():
    try:
        name, email, password, address, pincode = "Doggie", "doggie@doggie.com", "doggie", "SFDS", 123456

        user = User.query.filter_by(email=email).first()
        if user is not None:
            return

        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            address=address,
            pincode=int(pincode),
            role="ADMIN"
        )

        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(e)