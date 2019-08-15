import requests
import bs4


def tag_get(url):
    lg = requests.get(url).text
    soup = bs4.BeautifulSoup(lg, 'lxml')
    wo_tag = []
    for c in soup.findAll('meta', {'property': 'instapp:hashtags'}):
        wo_tag.append(c.get('content'))
    return wo_tag
