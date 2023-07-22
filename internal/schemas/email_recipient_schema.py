from marshmallow import Schema, fields, validate

class EmailRecipientSchema(Schema):
    email = fields.String(required=True, validate=validate.Length(max=255))
