import requests
from bs4 import BeautifulSoup
import re

def scrape_menu_data():
    url = 'https://www.nandos.co.uk/food/menu/'  
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_pattern = re.compile(r'£\d+')
        elements = soup.find_all(text=price_pattern)

        for element in elements:
            print(f"Text: {element}")
            print(f"Parent: {element.parent.prettify()}")
            print('---')
    else:
        print('Failed to retreive the webpage')

if __name__ == "__main__":
    scrape_menu_data()