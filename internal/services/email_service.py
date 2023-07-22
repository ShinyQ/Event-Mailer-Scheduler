from internal.models.email import Email
from internal.utils.db import db
from internal.schemas.email_schema import EmailSchema


class EmailService:
    @staticmethod
    def create_email(data):
        try:
            errors = EmailSchema().validate(data)

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
        except Exception as e:
            print(f"Error while creating email: {e}")
            return None, f"Error while creating email: {e}"

    @staticmethod
    def get_email_list():
        try:
            emails = Email.query.all()
            email_list = EmailSchema(many=True).dump(emails)

            return email_list, None
        except Exception as e:
            print(f"Error while serializing email data: {e}")
            return None, f"Error while serializing email data: {e}"
