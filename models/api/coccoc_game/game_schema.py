from marshmallow import Schema, fields, validate, validates, ValidationError

from models.api.coccoc_game.categories import Categorychema


class GameSchema(Schema):
    category_schema = Categorychema()

    game_id = fields.Int(required=True, allow_none=False,)
    game_name = fields.Str(required=True, allow_none=False,)
    iframe = fields.Int(required=True, allow_none=False)
    game_url = fields.Str(required=True, allow_none=False, validate=validate.URL(error="Not a valid URL"))
    page_url = fields.Str(required=True, allow_none=False, validate=validate.URL(error="Not a valid URL"))
    thumb_image_url = fields.Str(required=True, allow_none=True, validate=validate.URL(error="Not a valid URL"))
    image_url = fields.Str(required=True, allow_none=True, validate=validate.URL(error="Not a valid URL"))
    description = fields.Str(required=True, allow_none=True)
    categories = fields.List(fields.Nested(category_schema), required=True, allow_none=False)



