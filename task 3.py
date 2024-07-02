import requests
from bs4 import BeautifulSoup
import pandas as pd


# This example will demonstrate the basic principles.


# For this example, let's scrape data from a sample web page.
url = 'https://www.wikipedia.org/'  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    

    # For demonstration, let's extract all the hyperlinks from the page.
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text
        links.append({'text': text, 'url': href})
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(links)
    
    # Display the DataFrame
    print(df)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

# You can further manipulate and save the data using pandas if needed.
# For example, saving the data to a CSV file:
df.to_csv('scraped_links.csv', index=False)
