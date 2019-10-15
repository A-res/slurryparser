#!/usr/bin/env python3
import urllib.request
import re
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    grid = soup.findAll('', class_="dz_product-item-title")
    titles_list = []
    for i in grid:
        f = str(i.find_all('a'))
        f = (f[f.find('title=') + 6:])
        f = re.findall(r'"(.*?)"', f)
        print(f)
        titles_list.append(f)

def main():
    adress_def = 'https://vapeliga.ru/'
    for p in range(31):
      adress=adress_def+('zhidkosti_usa/filter/clear/apply/?PAGEN_1='+str(p))
      parse(get_html(adress))
      print(adress)

      for k in range (61):
          adress = adress_def + ('zhidkosti_rossiya/filter/clear/apply/?PAGEN_1=' + str(k))
          parse(get_html(adress))
          print(adress)

      #print(parse)
if __name__ == '__main__':
    main()