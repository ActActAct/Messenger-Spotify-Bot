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

# Print response
print(response.json())
