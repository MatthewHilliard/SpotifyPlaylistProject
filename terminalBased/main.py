import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import openai

openai.api_key = "YOUR API KEY"

scope='playlist-modify-public'
username = input("Spotify Username: ")

token = SpotifyOAuth(scope=scope, username=username)
sp = spotipy.Spotify(auth_manager = token)

theme = input("Playlist Theme: ")
sp.user_playlist_create(username, theme, True, False, "New Playlist")

numSongs = input("Number of Songs (max 50): ")
while int(numSongs) > 50:
    numSongs = input("Number of Songs (max 50): ")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  max_tokens=1000,
  temperature=0,
  messages=[
    {"role": "system", "content": "You are an assistant that only responds in JSON. Create a list of unique songs based off the user given theme. Include title and artist in your response. An example response is: title: Clocks artist: Coldplay."},
    {"role": "user", "content": "The theme is {0}. Create a list of {1} songs.".format(theme, numSongs)}
  ]
)
content = json.loads(response.choices[0].message.content)

songs_list = []
for i in range(int(numSongs)):
    currSong = content['songs'][i]['title']
    currArtist = content['songs'][i]['artist']
    q = "artist:{0} track:{1}".format(currArtist, currSong)
    results = sp.search(q)
    if len(results["tracks"]["items"]) != 0:
      songs_list.append(results["tracks"]["items"][0]["uri"])
    else:
       q = "track:{0}".format(currSong)
       results = sp.search(q)
       if len(results["tracks"]["items"]) != 0:
        songs_list.append(results["tracks"]["items"][0]["uri"])

playlist_id = sp.user_playlists(username)["items"][0]["id"]

sp.user_playlist_add_tracks(username, playlist_id, songs_list)