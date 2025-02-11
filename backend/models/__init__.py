from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

# Define Models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    joined_on = db.Column(db.Date, default=date.today())
    role = db.Column(db.String, db.CheckConstraint("role IN ('CUSTOMER', 'REG_PROFESSIONAL', 'PROFESSIONAL', 'ADMIN')"), default='CUSTOMER')
    mobile = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, db.CheckConstraint("status IN ('BLOCKED', 'ALLOWED')"), default='ALLOWED')

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Professional(db.Model):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, db.CheckConstraint("status IN ('REJECTED', 'PENDING', 'ACCEPTED', 'BLOCKED')"), default='PENDING')
    rating = db.Column(db.Integer, default=0)
    service = db.relationship('Service', back_populates='professionals')

Service.professionals = db.relationship('Professional', order_by=Professional.id, back_populates='service')

class ServiceRequest(db.Model):
    __tablename__ = 'service_request'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String, nullable=False)
    status = db.Column(db.String, db.CheckConstraint("status IN ('REJECTED', 'PENDING', 'ACCEPTED')"), default='PENDING')
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    remarks = db.Column(db.Text)
    customer_rating = db.Column(db.Integer, db.CheckConstraint('customer_rating BETWEEN 1 AND 5'))
    review = db.Column(db.Text)
