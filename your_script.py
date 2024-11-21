import argparse
import requests
import json
import os
import pandas as pd
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(description='Tourism and Cultural Event Insights')
    parser.add_argument('--static', nargs='?', const='static_data', help='Static Mode: Provide path to static dataset(s)')
    parser.add_argument('--scrape', action='store_true', help='Scrape Mode: Perform scraping and API requests for a few select elements')

    args = parser.parse_args()

    if args.static:
        static_mode(args.static)
    elif args.scrape:
        scrape_mode()
    else:
        default_mode()

def fetch_weather_data():
    print("Fetching weather data from OpenWeatherMap...")
    
    # Your OpenWeatherMap API key - replace with your actual key
    API_KEY = "f78d7dbedca1586e4111c6df97cee2a8"  # Get this from OpenWeatherMap
    city = "Los Angeles"
    
    # Construct the URL with proper API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        weather_data = response.json()
        
        # Extract relevant weather information
        weather_info = {
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
        
        print("Successfully fetched weather data")
        return weather_info
        
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}

def get_foursquare_data(limit=5):
    print("Fetching data from Foursquare API...")
    LA_longitude_latitude = "34.0549,118.2426"
    radius = 100000
    url = f"https://api.foursquare.com/v3/places/search?ll={LA_longitude_latitude}&radius={radius}&limit={limit}"

    headers = {
        "accept": "application/json",
        "Authorization": "fsq36Bc3bgBPQ0UBFV+zbcjOoxVkvhzrUgeEaZBAP0IQ4Hg="  # Replace with your Foursquare API key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        places = []
        for place in data.get('results', []):
            places.append({
                'Name': place.get('name'),
                'Address': ', '.join(place.get('location', {}).get('formatted_address', '')),
                'Category': place.get('categories')[0].get('name') if place.get('categories') else 'N/A'
            })
        print(f"Successfully fetched {len(places)} places from Foursquare.")
        return places
    except requests.RequestException as e:
        print(f"Error fetching Foursquare data: {e}")
        return []

def scrape_events(limit=5):
    """Scrape events from AllEvents.in for Los Angeles."""
    print("Scraping data from AllEvents.in...")
    URL = "https://allevents.in/los%20angeles"
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        events = []

        # Select the event cards
        event_cards = soup.select('li.event-card')[:limit]
        if not event_cards:
            print("No event data found. The structure of the page might have changed.")
            return []

        # Extract details for each event
        for event in event_cards:
            title = event.select_one('div.title h3').text.strip() if event.select_one('div.title h3') else 'No title'
            location = event.select_one('div.subtitle').text.strip() if event.select_one('div.subtitle') else 'No location'
            date = event.select_one('div.date').text.strip() if event.select_one('div.date') else 'No date'
            events.append({'Title': title, 'Location': location, 'Date': date})

        print(f"Successfully scraped {len(events)} events.")
        return events
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def save_static_data(weather_data, foursquare_data, events_data):
    print("Saving data to static files...")
    STATIC_DATASET_DIR = 'static_data'
    os.makedirs(STATIC_DATASET_DIR, exist_ok=True)
    
    # Save weather data
    weather_file = os.path.join(STATIC_DATASET_DIR, 'weather_data.json')
    with open(weather_file, 'w') as f:
        json.dump(weather_data, f, indent=4)
    print(f"Weather data saved to {weather_file}")

    # Save Foursquare data to CSV
    foursquare_file = os.path.join(STATIC_DATASET_DIR, 'foursquare_data.csv')
    df_places = pd.DataFrame(foursquare_data)
    df_places.to_csv(foursquare_file, index=False)
    print(f"Foursquare data saved to {foursquare_file}")

    # Save events data to CSV
    events_file = os.path.join(STATIC_DATASET_DIR, 'events_data.csv')
    df_events = pd.DataFrame(events_data)
    df_events.to_csv(events_file, index=False)
    print(f"Events data saved to {events_file}")

def print_data_samples(weather_data, foursquare_data, events_data):
    print("\nSample Data:")
    print("\nWeather Data:")
    print(json.dumps(weather_data, indent=4))

    print("\nFoursquare Data (first 5 places):")
    for place in foursquare_data[:5]:
        print(json.dumps(place, indent=4))

    print("\nEvents Data (first 5 events):")
    for event in events_data[:5]:
        print(json.dumps(event, indent=4))

def default_mode():
    print("Running in Default Mode...")
    weather_data = fetch_weather_data()
    foursquare_data = get_foursquare_data(limit=10)
    events_data = scrape_events(limit=10)

    # Save data to static files
    save_static_data(weather_data, foursquare_data, events_data)

    # Print sample data
    print_data_samples(weather_data, foursquare_data, events_data)

def scrape_mode():
    print("Running in Scrape Mode...")
    weather_data = fetch_weather_data()
    foursquare_data = get_foursquare_data(limit=5)
    events_data = scrape_events(limit=5)

    # Print sample data
    print_data_samples(weather_data, foursquare_data, events_data)

def static_mode(static_path):
    print("Running in Static Mode...")
    # Assume static_path is a directory containing the static data files
    weather_file = os.path.join(static_path, 'weather_data.json')
    foursquare_file = os.path.join(static_path, 'foursquare_data.csv')
    events_file = os.path.join(static_path, 'events_data.csv')

    # Load data
    try:
        with open(weather_file, 'r') as f:
            weather_data = json.load(f)
        df_places = pd.read_csv(foursquare_file)
        df_events = pd.read_csv(events_file)
        # Convert DataFrame to list of dicts
        foursquare_data = df_places.to_dict('records')
        events_data = df_events.to_dict('records')
    except FileNotFoundError as e:
        print(f"Error loading static data: {e}")
        return

    # Print sample data
    print_data_samples(weather_data, foursquare_data, events_data)

if __name__ == '__main__':
    main()
