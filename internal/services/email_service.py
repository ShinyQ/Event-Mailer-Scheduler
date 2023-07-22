from internal.models.email import Email
from internal.utils.db import db
from internal.schemas.email_schema import EmailSchema

email_schema = EmailSchema()


class EmailService:
    @staticmethod
    def create_email(data):
        errors = email_schema.validate(data)
        if errors:
            return None, errors

        event_id = data['event_id']
        email_subject = data['email_subject']
        email_content = data['email_content']
        timestamp = data['timestamp']

        email = Email(
            event_id=event_id,
            email_subject=email_subject,
            email_content=email_content,
            timestamp=timestamp
        )

        db.session.add(email)
        db.session.commit()

        return email, None
