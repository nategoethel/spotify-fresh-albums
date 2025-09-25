import re
from urllib.parse import urlparse


class Album:
    def __init__(self, title, artist, domain, url_override):
        self.title = title
        self.artist = artist
        self.domain = domain
        self.url_override = url_override

    def get_album_id(self):
        """if the domain is spotify, we can get the id. otherwise return None"""
        if "spotify" in self.domain:
            # the url format looks like this: https://open.spotify.com/album/6y6GXxqwsAT6JfiAI3nnLg?si=b9OAP1A5Teqxxwrb3Aa0Tg
            # in this example, 6y6GXxqwsAT6JfiAI3nnLg is the album id
            # spotify reference: https://developer.spotify.com/documentation/web-api/reference/get-an-album

            parsed_url = urlparse(self.url_override)
            path = parsed_url.path
            split_path = path.split("/")
            id = split_path[2]
            return id
        else:
            return None
