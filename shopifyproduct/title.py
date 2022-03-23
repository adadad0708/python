import requests
from bs4 import BeautifulSoup
import pandas as pd
wassersteinweb = []

url = "https://www.miasunny.com/collections/long-sleeves-dresses"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# image =  soup.find("div", {"class": "product-image__thumbs-content"}).find_all('img')

box = soup.find_all ( "div", {"class": "grid-product"} )
boxA = soup.find_all ( "a", {"class": "grid-product__image-link"} )
i = 0
for ds in boxA:

    ds = ds["href"]
    handle = ds.split('/')
    # handle = handle.pop ( -2 )
    print(handle,"handle")

    handle = handle[4]
    # handle = '/'.join ( handle )


    ds = "https://www.miasunny.com/" +ds

    rs = requests.get ( ds )
    soup2 = BeautifulSoup ( rs.content, 'lxml' )
    i = 0
    title= soup2.find ( "h1", {"class": "product-single__title"} ).get_text().strip()
    element_info = {
        'Title': title,

    }
    wassersteinweb.append ( element_info )

#     wassersteinweb.append ( element_info )
df = pd.DataFrame ( wassersteinweb )
# print (df)
df.to_csv ( 'title.csv' )