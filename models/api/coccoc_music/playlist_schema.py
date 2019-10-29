from marshmallow import Schema, fields, validate, validates, ValidationError

from models.api.coccoc_music.song_schema import SongSchema


class PlaylistSchema(Schema):

    song_schema = SongSchema()

    id = fields.Str(required=True, allow_none=False, validate=validate.Regexp('.+-playlist-+.*'))
    type = fields.Str(required=True, validate=validate.OneOf(['1', '2']), allow_none=False)
    genre = fields.Str(required=True, allow_none=True)
    name = fields.Str(required=True, allow_none=False)
    artists = fields.Str(required=True, allow_none=True)
    image = fields.Str(required=True, allow_none=True)
    items = fields.List(fields.Nested(song_schema), required=True, allow_none=False)

    @validates('name')
    def validate_name(self, value):
        if value == '':
            raise ValidationError('Name should not be blank')




