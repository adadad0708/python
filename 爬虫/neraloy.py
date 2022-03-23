import requests
from bs4 import BeautifulSoup

url = "https://www.neraloy.com/products/mens-swim-shorts-summer-colorful-swimwear"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
image =  soup.find("div", {"class": "swiper-container"}).find_all('img')
num = 0
for images in image:
    images = (images['src'])
    a = requests.get ( images )
    with open ( r'E:\新品杂货\2022\0311\02\{}.jpg'.format ( num ), 'wb' ) as f:
        f.write ( a.content )  # 二进制
        num += 1