from marshmallow import Schema, fields, validate


class EmailSchema(Schema):
    event_id = fields.Integer(required=True)
    email_subject = fields.String(required=True, validate=validate.Length(max=255))
    email_content = fields.String(required=True)
    timestamp = fields.DateTime(required=True)
