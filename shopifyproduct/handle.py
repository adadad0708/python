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
    print(handle,"handle")

    ds = "https://www.miasunny.com/" +ds

    rs = requests.get ( ds )
    soup2 = BeautifulSoup ( rs.content, 'lxml' )
    optionB = soup2.find ( "label", {"for": "ProductSelect--product-template-option-1"} ).text.strip ()
    print (optionB, "optionB" )

    optionBval = soup2.find ( "fieldset", {"name": "size"} ).find_all ("label" )
    title = soup2.find ( "h1", {"class": "product-single__title"} ).get_text ().strip ()

    imga = soup2.find ( "div", {"class": "product-single__thumbnails"} )
    if imga:

        img = imga.find_all ( "img" )
    # if optionB:
    #
    #     for optionBval in optionBval:
    #         optionBval = optionBval.text
    #         print ( optionBval, "optionBval" )
    print ( len(optionBval),"len(optionBval)" )
    print ( len(img),"len(img)" )

    if len(optionBval)>len(img):
        for optionBval in optionBval:
            element_info = {
                'Handle': handle,
                'Title': title,

            }
            wassersteinweb.append ( element_info )
    else :
        for img in img:
            element_info = {
                'Handle': handle,
                'Title': title,

            }
            wassersteinweb.append ( element_info )



#     wassersteinweb.append ( element_info )
df = pd.DataFrame ( wassersteinweb )
# print (df)
df.to_csv ('haqndwle.csv')