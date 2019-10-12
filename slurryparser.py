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
    #print(titles_list)


    #title=grid.find('h3')
    #print(grid)
#[f.find('title')+2:]
def main():
    parse(get_html('https://vapeliga.ru/zhidkosti_usa/filter/clear/apply/?PAGEN_1=4'))
    #print(parse)

if __name__ == '__main__':
    main()