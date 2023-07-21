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

Urls=["https://esimradar.com/esim-aland-islands/",
"https://esimradar.com/esim-albania/",
"https://esimradar.com/esim-andorra/",
"https://esimradar.com/esim-austria/",
"https://esimradar.com/esim-azores/",
"https://esimradar.com/esim-balearic-islands/",
"https://esimradar.com/esim-belarus/",
"https://esimradar.com/esim-belgium/",
"https://esimradar.com/esim-bosnia-and-herzegovina/",
"https://esimradar.com/esim-bulgaria/",
"https://esimradar.com/esim-canary-islands/",
"https://esimradar.com/esim-corfu/",
"https://esimradar.com/esim-crete/",
"https://esimradar.com/esim-croatia/",
"https://esimradar.com/esim-cyclades/",
"https://esimradar.com/esim-cyprus/",
"https://esimradar.com/esim-czech-republic/",
"https://esimradar.com/esim-denmark/",
"https://esimradar.com/esim-estonia/",
"https://esimradar.com/esim-faroe-islands/",
"https://esimradar.com/esim-finland/",
"https://esimradar.com/esim-france/",
"https://esimradar.com/esim-germany/",
"https://esimradar.com/esim-gibraltar/",
"https://esimradar.com/esim-greece/",
"https://esimradar.com/esim-guernsey/",
"https://esimradar.com/esim-hungary/",
"https://esimradar.com/esim-iceland/",
"https://esimradar.com/esim-ireland/",
"https://esimradar.com/esim-isle-of-man/",
"https://esimradar.com/esim-italy/",
"https://esimradar.com/esim-jersey/",
"https://esimradar.com/esim-kosovo/",
"https://esimradar.com/esim-latvia/",
"https://esimradar.com/esim-liechtenstein/",
"https://esimradar.com/esim-lithuania/",
"https://esimradar.com/esim-luxembourg/",
"https://esimradar.com/esim-macedonia/",
"https://esimradar.com/esim-madeira/",
"https://esimradar.com/esim-malta/",
"https://esimradar.com/esim-moldova/",
"https://esimradar.com/esim-monaco/",
"https://esimradar.com/esim-montenegro/",
"https://esimradar.com/esim-netherlands/",
"https://esimradar.com/esim-norway/",
"https://esimradar.com/esim-poland/",
"https://esimradar.com/esim-portugal/",
"https://esimradar.com/esim-rhodes/",
"https://esimradar.com/esim-romania/",
"https://esimradar.com/esim-russia/",
"https://esimradar.com/esim-san-marino/",
"https://esimradar.com/esim-sardinia/",
"https://esimradar.com/esim-scotland/",
"https://esimradar.com/esim-serbia/",
"https://esimradar.com/esim-sicily/",
"https://esimradar.com/esim-slovakia/",
"https://esimradar.com/esim-slovenia/",
"https://esimradar.com/esim-spain/",
"https://esimradar.com/esim-svalbard-and-jan-mayen/",
"https://esimradar.com/esim-sweden/",
"https://esimradar.com/esim-switzerland/",
"https://esimradar.com/esim-ukraine/",
"https://esimradar.com/esim-united-kingdom/",
"https://esimradar.com/esim-vatican-city/",
"https://esimradar.com/esim-wales/",
"https://esimradar.com/esim-anguilla/",
"https://esimradar.com/esim-antigua-and-barbuda/",
"https://esimradar.com/esim-aruba/",
"https://esimradar.com/esim-bahamas/",
"https://esimradar.com/esim-barbados/",
"https://esimradar.com/esim-belize/",
"https://esimradar.com/esim-bermuda/",
"https://esimradar.com/esim-british-virgin-islands/",
"https://esimradar.com/esim-canada/",
"https://esimradar.com/esim-cayman-islands/",
"https://esimradar.com/esim-costa-rica/",
"https://esimradar.com/esim-curacao/",
"https://esimradar.com/esim-dominica/",
"https://esimradar.com/esim-dominican-republic/",
"https://esimradar.com/esim-el-salvador/",
"https://esimradar.com/esim-greenland/",
"https://esimradar.com/esim-grenada/",
"https://esimradar.com/esim-guatemala/",
"https://esimradar.com/esim-honduras/",
"https://esimradar.com/esim-jamaica/",
"https://esimradar.com/esim-martinique/",
"https://esimradar.com/esim-mexico/",
"https://esimradar.com/esim-montserrat/",
"https://esimradar.com/esim-nicaragua/",
"https://esimradar.com/esim-panama/",
"https://esimradar.com/esim-puerto-rico/",
"https://esimradar.com/esim-saint-barthelemy/",
"https://esimradar.com/esim-saint-kitts-and-nevis/",
"https://esimradar.com/esim-saint-lucia/",
"https://esimradar.com/esim-saint-martin/",
"https://esimradar.com/esim-saint-pierre-and-miquelon/",
"https://esimradar.com/esim-saint-vincent-and-the-grenadines/",
"https://esimradar.com/esim-trinidad-and-tobago/",
"https://esimradar.com/esim-turks-and-caicos-islands/",
"https://esimradar.com/esim-usa/",
"https://esimradar.com/esim-us-virgin-islands/",
"https://esimradar.com/esim-argentina/",
"https://esimradar.com/esim-bolivia/",
"https://esimradar.com/esim-brazil/",
"https://esimradar.com/esim-chile/",
"https://esimradar.com/esim-colombia/",
"https://esimradar.com/esim-ecuador/",
"https://esimradar.com/esim-falkland-islands/",
"https://esimradar.com/esim-french-guiana/",
"https://esimradar.com/esim-guyana/",
"https://esimradar.com/esim-paraguay/",
"https://esimradar.com/esim-peru/",
"https://esimradar.com/esim-suriname/",
"https://esimradar.com/esim-uruguay/",
"https://esimradar.com/esim-venezuela/",
"https://esimradar.com/esim-brunei/",
"https://esimradar.com/esim-cambodia/",
"https://esimradar.com/esim-indonesia/",
"https://esimradar.com/esim-laos/",
"https://esimradar.com/esim-malaysia/",
"https://esimradar.com/esim-myanmar/",
"https://esimradar.com/esim-philippines/",
"https://esimradar.com/esim-singapore/",
"https://esimradar.com/esim-thailand/",
"https://esimradar.com/esim-vietnam/",
"https://esimradar.com/esim-afghanistan/",
"https://esimradar.com/esim-armenia/",
"https://esimradar.com/esim-azerbaijan/",
"https://esimradar.com/esim-bangladesh/",
"https://esimradar.com/esim-bhutan/",
"https://esimradar.com/esim-china/",
"https://esimradar.com/esim-georgia/",
"https://esimradar.com/esim-hong-kong/",
"https://esimradar.com/esim-india/",
"https://esimradar.com/esim-japan/",
"https://esimradar.com/esim-kazakhstan/",
"https://esimradar.com/esim-kyrgyzstan/",
"https://esimradar.com/esim-macau/",
"https://esimradar.com/esim-maldives/",
"https://esimradar.com/esim-mongolia/",
"https://esimradar.com/esim-nepal/",
"https://esimradar.com/esim-pakistan/",
"https://esimradar.com/esim-south-korea/",
"https://esimradar.com/esim-sri-lanka/",
"https://esimradar.com/esim-taiwan/",
"https://esimradar.com/esim-tajikistan/",
"https://esimradar.com/esim-tibet/",
"https://esimradar.com/esim-uzbekistan/",
"https://esimradar.com/esim-bahrain/",
"https://esimradar.com/esim-iran/",
"https://esimradar.com/esim-iraq/",
"https://esimradar.com/esim-israel/",
"https://esimradar.com/esim-jordan/",
"https://esimradar.com/esim-kuwait/",
"https://esimradar.com/esim-oman/",
"https://esimradar.com/esim-qatar/",
"https://esimradar.com/esim-saudi-arabia/",
"https://esimradar.com/esim-turkey/",
"https://esimradar.com/esim-united-arab-emirates/",
"https://esimradar.com/esim-american-samoa/",
"https://esimradar.com/esim-australia/",
"https://esimradar.com/esim-fiji/",
"https://esimradar.com/esim-french-polynesia/",
"https://esimradar.com/esim-guam/",
"https://esimradar.com/esim-nauru/",
"https://esimradar.com/esim-new-zealand/",
"https://esimradar.com/esim-papua-new-guinea/",
"https://esimradar.com/esim-solomon-islands/",
"https://esimradar.com/esim-tonga/",
"https://esimradar.com/esim-algeria/",
"https://esimradar.com/esim-benin/",
"https://esimradar.com/esim-botswana/",
"https://esimradar.com/esim-burkina-faso/",
"https://esimradar.com/esim-burundi/",
"https://esimradar.com/esim-cape-verde/",
"https://esimradar.com/esim-cameroon/",
"https://esimradar.com/esim-central-african-republic/",
"https://esimradar.com/esim-chad/",
"https://esimradar.com/esim-congo/",
"https://esimradar.com/esim-democratic-republic-of-the-congo/",
"https://esimradar.com/esim-egypt/",
"https://esimradar.com/esim-eswatini/",
"https://esimradar.com/esim-ethiopia/",
"https://esimradar.com/esim-gabon/",
"https://esimradar.com/esim-gambia/",
"https://esimradar.com/esim-ghana/",
"https://esimradar.com/esim-guinea-bissau/",
"https://esimradar.com/esim-guinea/",
"https://esimradar.com/esim-ivory-coast/",
"https://esimradar.com/esim-kenya/",
"https://esimradar.com/esim-lesotho/",
"https://esimradar.com/esim-liberia/",
"https://esimradar.com/esim-madagascar/",
"https://esimradar.com/esim-malawi/",
"https://esimradar.com/esim-mali/",
"https://esimradar.com/esim-mauritania/",
"https://esimradar.com/esim-mauritius/",
"https://esimradar.com/esim-mayotte/",
"https://esimradar.com/esim-morocco/",
"https://esimradar.com/esim-mozambique/",
"https://esimradar.com/esim-namibia/",
"https://esimradar.com/esim-niger/",
"https://esimradar.com/esim-nigeria/",
"https://esimradar.com/esim-reunion/",
"https://esimradar.com/esim-rwanda/",
"https://esimradar.com/esim-senegal/",
"https://esimradar.com/esim-seychelles/",
"https://esimradar.com/esim-sierra-leone/",
"https://esimradar.com/esim-somalia/",
"https://esimradar.com/esim-south-africa/",
"https://esimradar.com/esim-sudan/",
"https://esimradar.com/esim-tanzania/",
"https://esimradar.com/esim-togo/",
"https://esimradar.com/esim-tunisia/",
"https://esimradar.com/esim-uganda/",
"https://esimradar.com/esim-zambia/",
"https://esimradar.com/esim-zimbabwe/",]

for u in Urls:
    table_url = u
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