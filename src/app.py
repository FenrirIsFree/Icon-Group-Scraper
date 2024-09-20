from get_DB_HTML import get_site_html

base_url = 'https://www.dannyboyspizza.com/'

site_name, success = get_site_html(base_url)

if success:
    print(site_name, success)
else:
    print('Error fetching the website')

