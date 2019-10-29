from marshmallow import Schema, fields, validate, validates, ValidationError


class SongSchema(Schema):
    id = fields.Str(required=True, allow_none=False, validate=validate.Regexp('.+-song-+.*'))
    type = fields.Str(required=True, allow_none=False, validate=validate.OneOf(['1', '2']))
    title = fields.Str(required=True, allow_none=False)
    url = fields.Str(required=True, allow_none=False, validate=validate.URL(error="Not a valid URL"))
    artists = fields.Str(required=True, allow_none=True)
    image = fields.Str(required=True, allow_none=True)

    @validates('title')
    def validate_title(self, value):
        if value == '':
            raise ValidationError('Title should not be blank')
        elif value == 'null':
            raise ValidationError('Why are you doing like this, convert value to string "null" ')

    @validates('artists')
    def validate_artists(self, value):
        if value == 'null':
            raise ValidationError('Why are you doing like this, convert value to string "null" ')

    @validates('image')
    def validate_image(self, value):
        if value == 'null':
            raise ValidationError('Why are you doing like this, convert value to string "null" ')



