import pylab as p
import requests
from bs4 import BeautifulSoup
import pandas as pd



wassersteinweb = []

url = "https://www.levoisy.com/collections/birds"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# image =  soup.find("div", {"class": "product-image__thumbs-content"}).find_all('img')
HTML = '''<p data-mce-fragment="1"><strong data-mce-fragment="1">🎉GIVE A GIFT🎁THAT IS MEANINGFUL AND MEMORABLE!</strong></p><p data-mce-fragment="1">Handmade</p><p data-mce-fragment="1">Height:6 inches</p><p data-mce-fragment="1">Width:4 inches</p><p data-mce-fragment="1">Materials:wood</p><p data-mce-fragment="1">Our glasses holders are so adorable,they will keep you smiling and happy every time you look at them on your desk!</p><p data-mce-fragment="1">These eyeglass stands will be your eyeglasses'best friend.</p><p>Keep your glasses where you can find them–with style,charm,and personality!</p><p data-mce-fragment="1">An eyeglass accessory that will keep your glasses safe and add a smile to your day.</p><p data-mce-fragment="1">This eyeglass accessory keeps your glasses safe and adds a sense of whimsy to any desk,table,or shelf.</p><span data-mce-fragment="1">Have animals fanned in the family?We have a glasses stand for everyone!Each one is carefully hand-painted by me.No two will ever be exactly alike since they are done by hand.</span>'''
comPrice =  soup.find_all("span", {"class": "dj_skin_product_compare_at_price"})
for comPrice in comPrice:
    comPrice =  comPrice.text


title = soup.find_all ( "a", {"class": "product-snippet__title-normal"} )

price = soup.find_all ( "span", {"class": "dj_skin_product_price"} )



images = soup.find ( "div", {"class": "collection-product__wrapper"} ).find_all ( 'img' )









for images in images:
    images = images["data-src"]
    images = images.replace ( '{width}', '720' )
    images = "https:" + images
    print ( images )
for price in price:
    price = price.text
    price = price.replace ( '$', '' )
for title in title:
    titles = title.text
    print ( title )
    titles = titles.replace ( "[Women's Day Gift] ", '' )
    element_info = {
    'Title': titles,
        'Body (HTML)': HTML,
        'Variant Taxable': 'FALSE',
        'Vendor':"bird",
        'Tags': 'Dogs',
    'Price': price,
    'Image Src': images,
    }

    wassersteinweb.append ( element_info )

df = pd.DataFrame ( wassersteinweb )

df.to_csv ('titles66.csv')