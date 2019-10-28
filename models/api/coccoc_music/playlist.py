from typing import Optional
import array


class Playlist(object):
    id: str
    type: str
    genre: Optional[str]
    name: str
    artists: Optional[str]
    image: Optional[str]
    items: array


