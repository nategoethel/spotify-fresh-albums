# The idea is that this script will:
# 1. Send a request to the Reddit API to get all of the new posts in /r/hiphopheads that have "[FRESH ALBUM]" in their title.
# 2. Parse the list of results, extracting the artist name and album title.
# 3. Use the Spotify API to search for the album and add it to my Listen Later playlist if it's found.

import requests
import requests.auth
import os
import json
from dotenv import load_dotenv
from classes import Album

REDDIT_API_BASE = "https://oauth.reddit.com"
REDDIT_USER_AGENT = "spotify-fresh-albums by myshortfriend"


load_dotenv()


def authorize_reddit():
    """returns a token"""
    username = os.getenv("REDDIT_USER_NAME")
    password = os.getenv("REDDIT_PASSWORD")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")

    # build request
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": REDDIT_USER_AGENT}

    resp = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=client_auth,
        data=post_data,
        headers=headers,
    )
    resp_data = resp.json()
    token = resp_data["access_token"]

    return token


def search_reddit(token: str):
    """make a request to the Reddit search API"""
    query_string = "[FRESH+ALBUM]"
    album_list = []

    # build request. we need to use restrict_sr here to keep the results limited to the subreddit we pass in the request URL
    # without restrict_sr, the Reddit API will return results from all across reddit.
    headers = {"Authorization": f"bearer {token}", "User-Agent": REDDIT_USER_AGENT}
    params = {
        "q": query_string,
        "type": "posts",
        "sort": "top",
        "t": "week",
        "restrict_sr": True,
        "limit": 10,
    }

    # send request to the /search endpoint: https://www.reddit.com/dev/api/#GET_search
    response = requests.get(
        REDDIT_API_BASE + "/r/hiphopheads/search/?", params=params, headers=headers
    )

    resp_data = response.json()

    # get all results from the `children` key
    posts = resp_data["data"]["children"]

    # the fields we're interested in are: title, domain, and url_overridden_by_dest
    for post in posts:
        data = post["data"]    
        title = data.get('title', None)
        domain = data.get('domain', None)
        url_overridden_by_dest = data.get('url_overridden_by_dest', None)

        album = Album(title=title, domain=domain, url_override=url_overridden_by_dest)
        album_list.append(album)

        print(album.name)


def search_spotify():
    """make a request to the Spotify search API. Return the status code and the result."""
    pass


def add_album_to_playlist(album: Album):
    """adds the album to a playlist"""
    pass


def main():
    # get auth token
    token = authorize_reddit()

    # search reddit
    search_reddit(token)


if __name__ == "__main__":
    main()
