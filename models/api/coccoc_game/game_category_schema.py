from marshmallow import Schema, fields, validate, validates, ValidationError

from models.api.coccoc_game.game_schema import GameSchema


class GameCategorySchema(Schema):
    game_schema = GameSchema()
    category_id = fields.Int(required=True, allow_none=False,)
    name = fields.Str(required=True, allow_none=False)
    games = fields.List(fields.Nested(game_schema), required=True, allow_none=False)
