# https://www.dannyboyspizza.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://www.dannyboyspizza.com/'
page_text = []

result = requests.get(base_url)
result_html = BeautifulSoup(result.text, 'html.parser')

print(result_html)