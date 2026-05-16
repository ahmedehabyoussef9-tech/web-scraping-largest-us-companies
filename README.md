# Web Scraping Largest US Companies

## Overview
This project uses Python web scraping techniques to extract data from a Wikipedia table containing the largest companies in the United States by revenue. The extracted data is cleaned, structured into a pandas DataFrame, and exported as a CSV file.

## Tools & Libraries Used
- Python
- BeautifulSoup4
- Requests
- pandas

## Features
- Sends HTTP requests to a webpage
- Parses HTML content using BeautifulSoup
- Extracts table headers and row data
- Stores data in a pandas DataFrame
- Exports cleaned data to CSV format

## Project Workflow
1. Send a request to the target webpage
2. Parse webpage HTML content
3. Locate and extract the target table
4. Extract column names and row data
5. Store extracted data into a pandas DataFrame
6. Export the dataset as a CSV file

## Files Included
- `web_scraping_project.py` — Main Python script
- `List of largest companies in the United States by revenue.csv` — Extracted dataset

## Dataset Source
Wikipedia:
https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue

## Skills Demonstrated
- Web scraping
- HTML parsing
- Data extraction
- Data cleaning
- Data handling with pandas
- CSV export automation
