import requests
from pyquery import PyQuery as pq
import json
import re
from mongo import DB

url = 'http://mag234.com/index/index?c=&k='

class send:
    def __init__(self, url):
        self.doc = pq(requests.get(url).content.decode())('.link-list-wrapper')

class analyse:
    def __init__(self, doc):
        self.doc = doc('li')

    def getName(self, doc):
        return doc('.name').text()

    def getSize(self, doc):
        return doc('.size').text()

    def getLink(self, doc):
        return dict(
            mag = doc.attr('data-magnet'),
            ed2k = doc.attr('data-ed2k')
        )

    def json(self):
        obj = {}
        for i in self.doc.items():
            obj['name'] = self.getName(i)
            obj['size'] = self.getSize(i)
            obj['links'] = self.getLink(i)
            break
        return obj



def getAllPage(doc):
    page = doc('.pagination li')
    for i in page('a').items():
        if i.attr('aria-label') == 'Last':
            return i.attr('href').split('/')[-1]
    return len(page.text().replace(' ', ''))

def getLink(name):
    doc = send(url + name).doc
    linkList = doc('.link-list')
    page = getAllPage(doc)
    if not linkList.length:
        return
    print(json.dumps(analyse(linkList).json(), indent=2))


getLink('法医 朝颜')