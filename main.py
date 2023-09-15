import requests
import json

def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def fetch_top_song_from_playlist(access_token, playlist_link):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(playlist_link, headers=headers)
    with open("output.txt", "w") as file:
        json.dump(response.json(), file, indent=4)
    response.raise_for_status()
    data = response.json()
    top_song = data['tracks']['items'][0]['track']
    snapshot_id = data['snapshot_id']
    song_uri = top_song['uri']
    return top_song, snapshot_id, song_uri

def remove_song_from_playlist(access_token, playlist_id, song_uri, snapshot_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "tracks": [{"uri": song_uri}],
        "snapshot_id": snapshot_id
    }

    print(url, headers, data)
    response = requests.delete(url, headers=headers, json=data)

    print(response)
    return response.status_code == 200

if __name__ == "__main__":
    CLIENT_ID = "5972487482b145d183008a0ff7af682e"
    CLIENT_SECRET = "7411610ad87f42b9958d7472531dee9c"
    PLAYLIST_ID = "7gmLrKkw6OMl70O5Y2CEtM"
    PLAYLIST_LINK = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}?market=US'

    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    top_song, snapshot_id, song_uri = fetch_top_song_from_playlist(access_token, PLAYLIST_LINK)

    song_name = top_song['name']
    artist_name = top_song['artists'][0]['name']
    song_link = top_song['external_urls']['spotify']

    print(f"Song Name: {song_name}")
    print(f"Artist Name: {artist_name}")
    print(f"Song Link: {song_link}")

    if remove_song_from_playlist(access_token, PLAYLIST_ID, song_uri, snapshot_id):
        print("Song successfully removed from the playlist!")
    else:
        print("Error occurred while removing the song from the playlist.")

