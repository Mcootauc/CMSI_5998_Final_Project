Restaurant Data Analysis Script

Description
This script fetches top restaurants in Los Angeles from TripAdvisor and Yelp, then generates insights using the OpenAI API.
How to Run
Dependencies
Python 3.x

Install required packages:
pip install requests beautifulsoup4 pandas openai argparse

Execution Commands
Static Mode: Display data from static files.
python your_script.py --static <path/to/static_dataset_folder>
Scrape Mode: Scrape and fetch data for a few entries.
python your_script.py --scrape
Default Mode: Full data processing and analysis.
python your_script.py
Extensibility & Maintainability
Extensibility: Can be extended to other cities or include more data sources.
Maintainability: Update API keys and handle changes in API responses. Optimize code for larger datasets.
Modules Used
requests (HTTP requests)
beautifulsoup4 (Web scraping)
pandas (Data manipulation)
openai (OpenAI API access)
argparse (Command-line argument parsing)
Approximate Run Times
Static Mode: Less than 1 minute
Scrape Mode: Approximately 2 minutes
Default Mode: Approximately 5 minutes
