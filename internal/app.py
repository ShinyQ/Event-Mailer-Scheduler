from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from internal.utils.db import init_db, db  # Import the db instance

from .views.email_controller import email_bp

load_dotenv()


def create_app():
    app = Flask(__name__)
    init_db(app)

    # Use the db instance here instead of the db module from internal.utils
    Migrate(app, db)

    app.register_blueprint(email_bp)

    # Global error handler for 500 Internal Server Error
    @app.errorhandler(500)
    def handle_internal_server_error(e):
        print(e)
        return jsonify({"message": "Internal Server Error"}), 500

    # Global error handler for 404 Not Found
    @app.errorhandler(404)
    def handle_not_found_error(e):
        return jsonify({"message": "Not Found"}), 404

    # Global error handler for 405 Method Not Allowed
    @app.errorhandler(405)
    def handle_method_not_allowed_error(e):
        return jsonify({"message": "Method Not Allowed"}), 405

    return app
