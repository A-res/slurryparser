#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    grid = soup.findAll('', class_="dz_product-item-title")
    titles_list = []
    for row in grid:
        f =row.get('title')
        titles_list.append(f)
    print(titles_list)
    #title=grid.find('h3')
    print(grid)

def main():
    parse(get_html('https://vapeliga.ru/zhidkosti_usa/'))
    print(parse)

if __name__ == '__main__':
    main()