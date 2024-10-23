import sqlite3
from flask import g

DATABASE = 'services.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # Create the professional table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS professional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                experience INTEGER NOT NULL,
                description TEXT,
                estimated_time INTEGER NOT NULL,
                visiting_charge INTEGER DEFAULT 0,
                date_joined DATE DEFAULT CURRENT_DATE
            )
        ''')

        # Create the user table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT DEFAULT 'customer' CHECK( role IN ('customer','admin') ) NOT NULL
            )
        ''')

        # Create the service table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS service (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                estimated_time INTEGER NOT NULL,
                visiting_charge INTEGER DEFAULT 0
            )
        ''')

        # Create the service_request table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_request (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_id INTEGER NOT NULL,
                customer_id INTEGER NOT NULL,
                professional_id INTEGER NOT NULL,
                date_of_request TEXT NOT NULL,
                date_of_completion TEXT,
                service_status TEXT CHECK(service_status IN ('requested', 'assigned', 'closed', 'cancelled')) NOT NULL,
                remarks TEXT,
                FOREIGN KEY (service_id) REFERENCES service(id),
                FOREIGN KEY (customer_id) REFERENCES user(id),
                FOREIGN KEY (professional_id) REFERENCES professional(id)
            )
        ''')

        # Create the reviews table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS review (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_request_id INTEGER,
                rating INTEGER CHECK (rating BETWEEN 1 AND 5),
                remarks TEXT,
                FOREIGN KEY (service_request_id) REFERENCES service_request(id)
            )
        ''')

        db.commit()
