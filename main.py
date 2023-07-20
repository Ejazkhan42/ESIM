import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_table_with_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table with the desired data. You may need to inspect the website's HTML to get the table's specific attributes.
            table = soup.find('table')  # Replace 'your-table-class' with the actual class of the table.

            if table:
                rows = table.find_all('tr')
                data = []

                for idx, row in enumerate(rows):
                    if idx == 0 or idx == len(rows) - 1:  # Skip the first and last row
                        continue

                    # Extract the text content from each cell in the row
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]

                    # Extract the href links if they exist in the row
                    links = row.find_all('a', href=re.compile(r'^https?://'))  # Regex to match absolute URLs
                    href_links = [link['href'] for link in links]

                    # Combine the row data and href links into a single list
                    row_data.extend(href_links)

                    data.append(row_data)

                return data
            else:
                print("Table not found on the page.")
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return None

table_url = 'https://esimradar.com/esim-aland-islands/'
scraped_data = scrape_table_with_links(table_url)
data=[]
if scraped_data:
    # Load the existing CSV data (if any)
    try:
        existing_data = pd.read_csv('data.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    # Combine the existing data with the new scraped data
    new_data = pd.DataFrame(scraped_data)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Save the combined data to the 'data.csv' file
    combined_data.to_csv('data.csv', index=False)
    print("Data updated and saved successfully.")
else:
    print("Scraping failed.")
