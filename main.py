import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
data = []
def scrape_table_with_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table with the desired data. You may need to inspect the website's HTML to get the table's specific attributes.
            table = soup.find('table')  # Replace 'your-table-class' with the actual class of the table.

            if table:
                rows = table.find_all('tr')
                for r in range(1,len(rows)-1):
                    eSimProvider=rows[r].find_all('td')[0].find('picture').find('source')['srcset']
                    eSimProfile=rows[r].find_all('td')[1].text
                    eSimData=rows[r].find_all('td')[2].text
                    eSimValidity=rows[r].find_all('td')[3].text
                    eSimPriceGB=rows[r].find_all('td')[4].text
                    eSimPrice=rows[r].find_all('td')[5].text
                    eSimPhoneNumber=rows[r].find_all('td')[6].text
                    eSimCountry=rows[r].find_all('td')[7].text
                    eSimViews=rows[r].find_all('td')[8].find('a')['href']
                    ESIM={"Provder":eSimProvider,"eSIM Profile":eSimProfile,"Data":eSimData,"Validity":eSimValidity,
                          "Price/GB":eSimPriceGB,"Price":eSimPrice,"PhoneNumber":eSimPhoneNumber,"Country":eSimCountry,"View_Detail":eSimViews,}
                    data.append(ESIM)
                return data
            else:
                print("Table not found on the page.")
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return None

def combine_csv_files(file1, file2, output_file):
    df1 = pd.read_csv(file1)  # Read the first CSV file
    df2 = pd.DataFrame(file2)  # Read the second CSV file

    combined_df = pd.concat([df1, df2], ignore_index=True)  # Combine the two DataFrames

    combined_df.to_csv(output_file,index=False)  # Save the combined DataFrame to a new CSV file




table_url = 'https://esimradar.com/esim-aland-islands/'
scraped_data = scrape_table_with_links(table_url)
if data:
    try:
        file1 ='data.csv'
        output_file='data.csv'
        combine_csv_files(file1, data, output_file)
        print("Data updated and saved successfully.")
    except FileNotFoundError:
        df=pd.DataFrame(data)
        df.to_csv('data.csv',index=False)
        print("Datasaved successfully.")
else:
     print("Scraping failed.")