import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site


    def scrape(self):
        r = urllib.request.urlopen(self.site) #サイトからデータ取得
        html = r.read() #htmlのみが格納
        parser = "html.parser" #html情報を解析
        sp = BeautifulSoup(html, parser) 

        for tag in sp.find_all("a"): #aタグを集めてtag返す
            url = tag.get("href") #hrefの値だけを取り出す
            if url is None:
                continue
            print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()