import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import csv

# client_id and client_secret from Spotify for Developers
client_id = 'xxxx' 
client_secret = 'xxxx'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def download_img(track_id, spotify_id, genre):
    track_info = sp.track(spotify_id)
    album_info = track_info['album']
    
    img_url = album_info['images'][0]['url']

    genre_folder = os.path.join('album-covers', genre)

    if not os.path.exists(genre_folder):
        os.makedirs(genre_folder)

    response = requests.get(img_url)

    if response.status_code == 200:
        with open(os.path.join(genre_folder, f'{track_id}.png'), 'wb') as f:
            f.write(response.content)
    else:
        print('failed')
    
with open('filtered_info.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        track_id = row['track_id']
        spotify_id = row['spotify_id']
        genre = row['genre']
        
        download_img(track_id, spotify_id, genre)
