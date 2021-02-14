#!/usr/bin/python3 -B
# wikipedia.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote


def get_wiki_page(name):
    search_url = f'https://en.wikipedia.org/w/index.php?search={quote(name)}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.select_one('li.mw-search-result > div > a')
    if element == None:
        return response.url
    page_url = urljoin(search_url, soup.select_one('li.mw-search-result > div > a')['href'])
    return page_url


def get_political_party(url):
    pass

