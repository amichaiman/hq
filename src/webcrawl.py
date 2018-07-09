import re
import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def get_websites(url):
    html_text = get_raw_html(url)
    regex = re.compile(r'a href="http[^"]*"')
    url_set = set()
    for link in regex.findall(html_text):
        url_set.add(link[8:-1])
    return url_set


def get_html_text(url):
    request = requests.get(url)
    return request.content.__str__()


def get_raw_html(url):
    req = urllib.request.Request(url, headers=get_header())
    result = urllib.request.urlopen(req)
    return result.read().__str__()


def get_html(url):
    req = urllib.request.Request(url, headers=get_header())
    result = urllib.request.urlopen(req)
    soup = BeautifulSoup(result.read().decode('utf-8'), "lxml")
    return soup.get_text()


def google_search_result_websites(search_request):
    return get_websites(google_search_url(search_request))


def google_search_url(search_query):
    url = 'https://www.google.com/search?q='
    url += quote(search_query)
    return url


def get_header():
    headers = {
        'User-Agent': r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 '
                      r'Safari/537.36'}
    return headers
