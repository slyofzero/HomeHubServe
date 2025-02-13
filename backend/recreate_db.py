from app import db, app
from models import Professional, User
from sqlalchemy import text

with app.app_context():
    # query = f"DROP TABLE {Professional.__tablename__}"
    # db.session.execute(text(query))
    user = User.query.filter_by(email="1234567890").first()
    print(user)
    setattr(user, "role", "CUSTOMER")
    db.session.commit()