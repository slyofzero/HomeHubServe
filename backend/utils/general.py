from werkzeug.security import generate_password_hash
from models import db, User

def create_admin():
    try:
        name, mobile, password, address, pincode = "Doggie", "9876543210", "doggie", "SFDS", 123456

        user = User.query.filter_by(mobile=mobile).first()
        if user is not None:
            return

        new_user = User(
            name=name,
            mobile=mobile,
            password=generate_password_hash(password),
            address=address,
            pincode=int(pincode),
            role="ADMIN"
        )

        db.session.add(new_user)
        db.session.commit()
    except RuntimeError as e:
        print(e)