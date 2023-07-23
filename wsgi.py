from internal.app import new_app
from internal.utils.db import db

if __name__ == "__main__":
    new_app.run()

    @new_app.teardown_appcontext
    def shutdown_session():
        db.session.remove()
