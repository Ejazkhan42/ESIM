import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    "https://esimradar.com/esim-aland-islands/",
    "https://esimradar.com/esim-albania/",
    "https://esimradar.com/esim-andorra/",
    "https://esimradar.com/esim-austria/",
    "https://esimradar.com/esim-azores/",
    "https://esimradar.com/esim-balearic-islands/",
    "https://esimradar.com/esim-belarus/",
    "https://esimradar.com/esim-belgium/"
]

all_data = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        data.append(cols + [url])  # Append the URL as the last element of each row
    
    all_data.extend(data)

# Create a pandas DataFrame from the scraped data
df = pd.DataFrame(all_data, columns=["Provider", "eSIM Profile", "Data", "Validity", "Price/GB", "Price", "Phone Number", "Views"])

# Save the DataFrame to a CSV file
df.to_csv("table_data.csv", index=False)
