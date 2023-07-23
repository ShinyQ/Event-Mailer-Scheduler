from flask import Flask
from flask_migrate import Migrate
from .routers import Routers
from .utils.db import db, InitDB
from .utils.errors import ErrorHandling
from .utils.mailer import Mailer


def create_app():
    app = Flask(__name__)

    InitDB(app)
    Migrate(app, db)
    ErrorHandling(app)
    Mailer(app)
    Routers(app).init_routers()

    return app


new_app = create_app()
