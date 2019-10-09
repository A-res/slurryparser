#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parser(html):
    soup = BeautifulSoup(html)

def main():
    print(get_html('https://zenmod.ru/'))

if __name__ == '__main__':
    main()