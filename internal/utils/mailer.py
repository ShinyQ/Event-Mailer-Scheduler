from flask_mail import Mail, Message

from internal.utils.config import (
    MAIL_SENDER,
    MAIL_SERVER,
    MAIL_PORT,
    MAIL_USE_TLS,
    MAIL_USERNAME,
    MAIL_PASSWORD
)

class Mailer:
    mail = None

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    @staticmethod
    def init_app(app):
        app.config['MAIL_SERVER'] = MAIL_SERVER
        app.config['MAIL_PORT'] = MAIL_PORT
        app.config['MAIL_USERNAME'] = MAIL_USERNAME
        app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
        app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
        Mailer.mail = Mail(app)
     
     
def send_email(email_data):
    from internal.app import mailer
    message = Message(
        subject=email_data['subject'],
        sender=MAIL_SENDER,
        body=email_data['body'],
        recipients=[email_data['recipient']],
    )
    
    with mailer.mail.app.app_context():
        mailer.mail.send(message)
