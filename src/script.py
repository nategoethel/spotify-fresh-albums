# The idea is that this script will:
# 1. Send a request to the Reddit API to get all of the new posts in /r/hiphopheads that have "[FRESH ALBUM]" in their title.
# 2. Parse the list of results, extracting the artist name and album title.
# 3. Use the Spotify API to search for the album and add it to my Listen Later playlist if it's found.

import requests
import os
from classes import Album

def authorize_reddit():
    """returns a token"""
    pass

def search_reddit():
    """ make a request to the Reddit search API"""
    token = authorize_reddit()
    pass

def search_spotify():
    """make a request to the Spotify search API. Return the status code and the result."""
    pass

def add_album_to_playlist(album:Album):
    """adds the album to a playlist"""
    pass