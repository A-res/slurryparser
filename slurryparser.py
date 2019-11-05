#!/usr/bin/env python3
import urllib.request
import re
import csv
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def save(f,path):
    with open(path, 'a') as csvfile:
        fwriter = csv.writer(csvfile)
        fwriter.writerow(f)
       # fwriter.writerow(())

def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    grid = soup.findAll('', class_="dz_product-item-title")
    titles_list = []
    for i in grid:
        f = str(i.find_all('a'))
        f = (f[f.find('title=') + 6:])
        f = re.findall(r'"(.*?)"', f)
       # print(f)
        titles_list.append(f)
        save(f, 'slurries.csv')
        
def connectDB(db_file):
 conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def main():
    adress_def = 'https://vapeliga.ru/'
    for p in range(31):
      adress=adress_def+('zhidkosti_usa/filter/clear/apply/?PAGEN_1='+str(p))
      parse(get_html(adress))

      print('parsing 1st ' + str(int(p / 30 * 100)) + '%')

    for k in range (61):
         adress = adress_def + ('zhidkosti_rossiya/filter/clear/apply/?PAGEN_1=' + str(k))
         parse(get_html(adress))
         print('parsing 2nd '+str(int(k/ 60 * 100))+'%')

    for m in range(6):
        adress = adress_def + ('/zhidkosti_malaysia/filter/clear/apply/?PAGEN_1=' + str(m))
        parse(get_html(adress))
        print('parsing 3rd ' + str(int(m / 5 * 100)) + '%')

    for e in range(3):
        adress = adress_def + ('/zhidkosti_england/filter/clear/apply/?PAGEN_1=' + str(e))
        parse(get_html(adress))
        print('parsing 4th ' + str(int(e / 2 * 100)) + '%')



      #print(parse)
if __name__ == '__main__':
    main()