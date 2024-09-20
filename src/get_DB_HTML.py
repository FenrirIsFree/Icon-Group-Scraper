import requests
import json
import os

cwd = os.getcwd()
project_root = os.path.dirname(os.getcwd())

def get_site_html(base_url):
    
    site_name = base_url.split('.')[1]
    print(site_name)
    try:
        # Make a request to the website
        result = requests.get(base_url, timeout=10)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {base_url}: {e}")
        return None, False

    # Store the entire HTML content in a dictionary
    page_content = {'html': result.text}
    
    # Save the dictionary containing the HTML to a JSON file
    with open(f'{cwd}/cache/{site_name}.json', 'w', encoding='utf-8') as file:
        json.dump(page_content, file, indent=4, ensure_ascii=False)
    print('HTML content saved to DB_homepage_full_html.json')
    return site_name, True
    



