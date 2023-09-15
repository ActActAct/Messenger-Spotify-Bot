import requests
import json

playlist_link = 'https://api.spotify.com/v1/playlists/7gmLrKkw6OMl70O5Y2CEtM?market=US'
playlist_response = requests.get(playlist_link, headers=header)

with open('output.txt', 'w') as file:
        ile.write(json.dumps(playlist_response.json(), indent=4))