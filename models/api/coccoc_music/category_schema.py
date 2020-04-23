from marshmallow import Schema, fields


class CategorySchema(Schema):

    category_id = fields.Integer(required=True, allow_none=False,)
    name = fields.Str(required=True, allow_none=False)
    type = fields.Str(required=True, allow_none=False)
    image_url = fields.Str(required=True, allow_none=False)
    priority = fields.Integer(required=True, allow_none=True)


class ResultsCategorySchema(Schema):
    category_schema = CategorySchema()
    results = fields.List(fields.Nested(category_schema), required=True, allow_none=False)



