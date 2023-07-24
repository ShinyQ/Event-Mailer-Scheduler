from internal.app import app
from internal.utils.db import db

if __name__ == "__main__":
    app.run()

    @app.teardown_appcontext
    def shutdown_session():
        db.session.remove()
