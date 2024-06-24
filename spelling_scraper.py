# https://www.dannyboyspizza.com/
import requests
import re
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://www.dannyboyspizza.com/'

result = requests.get(base_url)
result_html = BeautifulSoup(result.text, 'html.parser')

# Find all the links in header of the homepage
header_links = []
header = result_html.header
links = header.find_all('li')

for link in links:
    header_links.append({
        'anchor name': link.find('a').get_text(strip=True),
        'anchor href': link.find('a')['href']
    })

# h1, h2, h3, h4, h5, h6, p, li
# Find all header text in the homepage
header_text = []
h1 = result_html.find_all('h1')
h1_count = 0
h2 = result_html.find_all('h2')
h2_count = 0
h3 = result_html.find_all('h3')
h3_count = 0
h4 = result_html.find_all('h4')
h4_count = 0
h5 = result_html.find_all('h5')
h5_count = 0
h6 = result_html.find_all('h6')
h6_count = 0

for h in h1:
    header_text.append({
        f'h1: {h1_count}': h.get_text()
    })
    h1_count += 1

for h in h2:
    header_text.append({
        f'h2: {h2_count}': h.get_text()
    })
    h2_count += 1

for h in h3:
    header_text.append({
        f'h3: {h3_count}': h.get_text()
    })
    h3_count += 1

for h in h4:
    header_text.append({
        f'h4: {h4_count}': h.get_text()
    })
    h4_count += 1

for h in h5:
    header_text.append({
        f'h5: {h5_count}': h.get_text()
    })
    h5_count += 1
 
for h in h6:
    header_text.append({
        f'h6: {h6_count}': h.get_text()
    })
    h6_count += 1

# Find all paragraph text in the homepage
paragraph_text = []
para = result_html.find_all('p')
p_count = 0

for p in para:
    paragraph_text.append({
        f'p: {p_count}': p.get_text()
    })
    p_count += 1

# Find all list text in the homepage
list_text = []
li = result_html.find_all('li')
li_count = 0

for l in li:
    # Use regex to replace \r, \n, and multiple spaces with a single space
    text = re.sub(r'[\r\n\s]+', ' ', l.get_text())
    list_text.append({
        f'li: {li_count}': text
    })
    li_count += 1