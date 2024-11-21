import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Constants
URL = "https://allevents.in/los%20angeles"
STATIC_DATASET_DIR = "static_data"
CSV_FILE = os.path.join(STATIC_DATASET_DIR, "allevents.csv")

def scrape_events():
    """Scrape the first 5 events from AllEvents.com."""
    print("Scraping data from AllEvents.com...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    events = []

    # Select the event cards
    event_cards = soup.select('li.event-card')[:10]
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

def save_events_to_csv(events):
    """Save scraped events to a CSV file."""
    print("Saving events to CSV...")
    os.makedirs(STATIC_DATASET_DIR, exist_ok=True)
    df = pd.DataFrame(events)
    df.to_csv(CSV_FILE, index=False)
    print(f"Events saved to {CSV_FILE}")

def main():
    events = scrape_events()
    if events:
        save_events_to_csv(events)

if __name__ == "__main__":
    main()
