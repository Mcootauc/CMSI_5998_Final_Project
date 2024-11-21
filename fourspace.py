import requests

# Los Angeles coordinates
LA_longitude_latitude = "34.0549,118.2426"
radius = 100000

url = f"https://api.foursquare.com/v3/places/search?ll={LA_longitude_latitude}&radius={radius}"

headers = {
    "accept": "application/json",
    "Authorization": "fsq36Bc3bgBPQ0UBFV+zbcjOoxVkvhzrUgeEaZBAP0IQ4Hg="
}

response = requests.get(url, headers=headers)

print(response.text)