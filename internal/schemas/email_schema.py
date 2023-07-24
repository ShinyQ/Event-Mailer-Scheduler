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
