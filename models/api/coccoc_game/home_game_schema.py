from marshmallow import Schema, fields, validate, validates, ValidationError

from models.api.coccoc_game.game_category_schema import GameCategorySchema
from models.api.coccoc_game.game_schema import GameSchema


class HomeGameSchema(Schema):

    class ResultsSchema(Schema):
        game_schema = GameSchema()
        game_category_schema = GameCategorySchema()

        highlighted = fields.List(fields.Nested(game_schema), required=True, allow_none=False)
        game_category = fields.List(fields.Nested(game_category_schema), required=True, allow_none=False)
        recommended = fields.List(fields.Nested(game_schema), required = True, allow_none = False)
    results = fields.Nested(ResultsSchema())
