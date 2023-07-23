from marshmallow import Schema, fields, validate, pre_load
from internal.utils.response import response_json
from datetime import datetime


class EmailSchema(Schema):
    event_id = fields.Integer(required=True)
    email_subject = fields.String(required=True, validate=validate.Length(max=255))
    email_content = fields.String(required=True)
    email_send_at = fields.DateTime(required=True)
    email_sent_at = fields.DateTime(required=False)
    created_at = fields.DateTime(required=False)

    @pre_load
    def validate_email_send_at(self, data, **kwargs):
        email_send_at = data.get('email_send_at')

        if email_send_at:
            try:
                email_send_at = datetime.strptime(email_send_at, '%Y-%m-%d %H:%M:%S')
                if email_send_at < datetime.utcnow():
                    response_json(None, 400, "Schedule time cannot be in the past")
            except ValueError:
                response_json(None, 500, "Invalid date format for email_send_at")

        return data
