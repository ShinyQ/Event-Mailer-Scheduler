from internal.utils.db import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)