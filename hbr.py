import requests
from bs4 import BeautifulSoup


def get_articles(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers) 
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('h2', {'class':"tm-title tm-title_h2"})[:5]
    d = {}
    for i in elements:
        title = i.text
        link = i.find('a', {'class':"tm-title__link"})['href']
        link = 'https://habr.com' + link
        d[title] = link
    return d       