from marshmallow import Schema, fields

from models.api.coccoc_game.game_schema import GameSchema


class NtpGamesSchema(Schema):

    class ResultsSchema(Schema):
        game_schema = GameSchema()

        highlighted = fields.List(fields.Nested(game_schema), required=True, allow_none=False)
        recommended = fields.List(fields.Nested(game_schema), required=True, allow_none=False)

    results = fields.Nested(ResultsSchema())
