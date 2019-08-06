import requests
import bs4
import json


def tag_get(url):
    lg = requests.get(url).text
    soup = bs4.BeautifulSoup(lg, 'lxml')
    c = soup.find(type= "application/ld+json")
    capt= json.loads(c.text)
    wo_tag = []
    for tg in capt['caption'].split(' '):
        if '#' in tg:
            wo_tag.append(tg.strip('#'))

    return wo_tag
