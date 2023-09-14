import requests

url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": "5972487482b145d183008a0ff7af682e",
    "client_secret": "7411610ad87f42b9958d7472531dee9c" 
}

response = requests.post(url, headers=headers, data=data)
access_token_json = response.json()
access_token = access_token_json['access_token']
header = {'Authorization': 'Bearer ' + access_token}


playlist_link = 'https://api.spotify.com/v1/playlists/7gmLrKkw6OMl70O5Y2CEtM?market=US'
playlist_response = requests.get(playlist_link, headers=header)

print(playlist_response.json())