from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Chrome/120.0.0.0 Safari/537.36)"
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html')

soup.find_all('table')[0]

soup.find('table', class_ = 'wikitable sortable')

# <table class="wikitable sortable jquery-tablesorter"> <caption>

table = soup.find_all('table')[0]

world_titles = table.find_all('th')

world_titles

world_table_titles = [title.text.strip() for title in world_titles]

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'C:\Users\astrr\OneDrive\Desktop\Data Analyst bootcamp\Web scraping\List of largest companies in the United States by revenue.csv', index = False)

df
