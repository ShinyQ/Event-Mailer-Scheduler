from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from internal.utils.db import init_db, db
from internal.utils.errors import global_errors_handler
from .views.email_controller import email_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    init_db(app)
    Migrate(app, db)
    global_errors_handler(app)

    app.register_blueprint(email_bp)

    return app
