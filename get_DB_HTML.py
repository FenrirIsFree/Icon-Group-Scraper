import requests
import json

base_url = 'https://www.dannyboyspizza.com/'

# Make a request to the website
result = requests.get(base_url)

# Store the entire HTML content in a dictionary
page_content = {'html': result.text}

# Save the dictionary containing the HTML to a JSON file
with open('DB_homepage_full_html.json', 'w', encoding='utf-8') as file:
    json.dump(page_content, file, indent=4, ensure_ascii=False)

print('HTML content saved to DB_homepage_full_html.json')