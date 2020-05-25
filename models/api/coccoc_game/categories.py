from marshmallow import Schema, fields


class Categorychema(Schema):
    category_id = fields.Int(required=True, allow_none=False,)
    name = fields.Str(required=True, allow_none=False)



