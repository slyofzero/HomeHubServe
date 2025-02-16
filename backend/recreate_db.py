from app import db, app
from models import Professional, User
from sqlalchemy import text

with app.app_context():
    query = f"DROP TABLE {Professional.__tablename__}"
    db.session.execute(text(query))
    query = f"DROP TABLE {User.__tablename__}"
    db.session.execute(text(query))
    db.session.commit()