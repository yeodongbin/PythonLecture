import requests
from bs4 import BeautifulSoup
def crawler(): 
    
    url = 'https://www.google.com'
    html = requests.get(url)
    soup = BeautifulSoup(html, 'html.parser')
    select = soup.head.find_all('meta')
    for meta in select:
        print(meta.get('content'))
crawler()