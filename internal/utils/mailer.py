from flask_mail import Mail, Message

class Mailer:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.mail = Mail(app)

        app.config['MAIL_SERVER'] = 'your_mail_server'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USERNAME'] = 'your_mail_username'
        app.config['MAIL_PASSWORD'] = 'your_mail_password'

    def send_email(self, subject, recipients, body):
        with self.app.app_context():
            message = Message(subject=subject, recipients=recipients, body=body)
            self.mail.send(message)
