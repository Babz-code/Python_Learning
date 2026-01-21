import requests
import lxml
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

date = input("Which year would you like to travel to? Enter your answer in this format 'YYYY-MM-DD'\n")

# TODO 1. Pulling data from Billboard
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url, headers=header)
website = response.text

soup = BeautifulSoup(website, "lxml")
song_title = soup.select("li ul li h3")
# artist_name = soup.select("ul li ul li span")

song_list = [song.getText().strip() for song in song_title]
# artist_list = [artist.getText().strip() for artist in artist_name]
# print(artist_list)

# TODO 2. Authenticating Spotify using spotipy
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                               redirect_uri="https://example.com/callback", show_dialog=True,
                                               cache_path="token.txt",
                                               username="Tbabz"))
user_id = sp.current_user()["id"]

year = date.split("-")[0]
# TODO 3. Search for songs on spotify using spotipy
song_uri = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"This {song} doesn't exist in the Spotify database, Skipped!")

# TODO 4. Create playlist using spotipy
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="Pulled from Billboard's data")
playlist_id = playlist["id"]

# TODO 5. Add songs to playlist
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)