# https://www.dannyboyspizza.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://www.dannyboyspizza.com/'
url = 'index'

# Find all the links in header of the homepage
header_links = []
counter = 1

while url:
    result = requests.get(f'{base_url}{url}')
    print(f'scraping {base_url}{url}...')
    result_html = BeautifulSoup(result.text, 'html.parser')
    header = result_html.header
    links = header.find_all('li')

    for link in links:
        header_links.append({
            'anchor name': link.find('a').get_text(strip=True),
            'anchor href': link.find('a')['href']
        })

    url = header_links[counter]['anchor href'] if counter < len(header_links) else None
    counter += 1
    sleep(2)

print(header_links)
# # Maybe easier way to grab data?
# # Initialize a dictionary to hold all headers
# headers = {}

# # List of header tags to search for
# header_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

# # Loop through each header tag and collect their texts
# for tag in header_tags:
#     headers[tag] = [h.get_text() for h in result_html.find_all(tag)]