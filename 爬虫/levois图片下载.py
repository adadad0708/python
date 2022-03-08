from bs4 import BeautifulSoup
import requests

def queryNewBalance():
    r = requests.get('https://www.levoisy.com/')
    soup = BeautifulSoup(r.content, 'html.parser')
    result = soup.find_all('a', class_='product-snippet__img-wrapper')
    for res in result:
         print(res.find('img', class_='serial-item-unveiling')["data-src"])
     # print(f"\nFound total shoes: {len(result)}")



queryNewBalance()

