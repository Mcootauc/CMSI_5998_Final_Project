# Tourism and Cultural Event Insights

## Project Overview

This project provides valuable insights for travelers by analyzing how weather impacts tourism patterns and local event attendance. By integrating data from multiple sources, the application forecasts how local attractions and events vary with seasonal changes, assisting both travelers and event organizers in making data-driven decisions.

## Features

- **Static Mode**: Load and display pre-saved datasets.
- **Scrape Mode**: Fetch and display sample data from APIs and web scraping.
- **Default Mode**: Perform full data fetching, processing, and output generation.

## Data Sources

1. **OpenWeatherMap API**: Provides weather data for various locations worldwide.
2. **Foursquare API**: Offers data on popular local venues, restaurants, and attractions.
3. **Eventbrite**: Scrapes data on local events, festivals, and cultural gatherings.


## Setup Instructions

### 1. Clone the Repository

### 2. Install Required Packages
   Required Packages:
      - pandas
      - requests
      - beautifulsoup4
      -argparse
      -time
### 3. Configure API Keys
Create a .env file with your API credentials: 
OPENWEATHERMAP_API_KEY=your_openweathermap_key
FOURSQUARE_CLIENT_ID=your_foursquare_id
FOURSQUARE_CLIENT_SECRET=your_foursquare_secret


## Extensibility & Maintainability
Extensible: Easily add new data sources or parameters.
Maintainable: Modular functions with error handling. Potential issues include API rate limits and data size constraints.

## Run Times
- Static Mode: <10 seconds
- Scrape Mode: ~30 seconds
- Default Mode: ~60 seconds


