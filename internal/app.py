from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from internal.utils.db import InitDB, db
from internal.utils.mailer import Mailer
from internal.utils.errors import ErrorHandling
from internal.routers import Routers

load_dotenv()

def create_app():
    app = Flask(__name__)

    Mailer(app)
    InitDB(app)
    Migrate(app, db)
    ErrorHandling(app)
    Routers(app).init_routers()

    return app
