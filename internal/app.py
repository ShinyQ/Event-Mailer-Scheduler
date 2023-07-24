from flask import Flask
from flask_migrate import Migrate
from .utils.mailer import Mailer

class App():
    app = None
    mailer = None

def create_app():
    modules = App()
    app = Flask(__name__)

    modules.app = app
    modules.mailer = Mailer(app)
    return modules


new_app = create_app()

app = new_app.app
mailer = new_app.mailer

from .routers import Routers
from .utils.db import db, InitDB
from .utils.errors import ErrorHandling

InitDB(app)
Migrate(app, db)
ErrorHandling(app)
Routers(app).init_routers()