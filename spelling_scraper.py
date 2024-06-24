# https://www.dannyboyspizza.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://www.dannyboyspizza.com/'
header_links = []
page_text = []

result = requests.get(base_url)
result_html = BeautifulSoup(result.text, 'html.parser')

# Find all the links in header of the homepage
header = result_html.header
links = header.find_all('li')

for link in links:
    header_links.append({
        'anchor name': link.find('a').get_text(strip=True),
        'anchor href': link.find('a')['href']
    })


print(header_links)