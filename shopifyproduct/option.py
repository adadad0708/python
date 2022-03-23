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
    title = soup2.find ( "h1", {"class": "product-single__title"} ).get_text ().strip ()

    optionA = soup2.find ( "label", {"for": "ProductSelect--product-template-option-0"} ).text.strip ()


    optionAval = soup2.find ( "fieldset", {"id": "ProductSelect--product-template-option-0"} ).find_all ("label" )
    if optionAval:
        for optionAval in optionAval:
            optionAval = optionAval.text
            print ( optionAval, "optionAval" )
    optionB = soup2.find ( "label", {"for": "ProductSelect--product-template-option-1"} ).text.strip ()

    optionBval = soup2.find ( "fieldset", {"id": "ProductSelect--product-template-option-1"} ).find_all ("label" )

    if optionB:
        element_info = {

            'Option1 Name': optionA,
            'Option2 Name': optionB,

        }
        wassersteinweb.append ( element_info )

        for optionBval in optionBval:
            optionBval = optionBval.text
            print ( optionBval, "optionBval" )
            element_info = {
                'Handle': handle,

                'Title': title,

                 'Option1 Value': optionAval,
                'Option2 Value': optionBval,


            }

            wassersteinweb.append ( element_info )
        df = pd.DataFrame ( wassersteinweb )
        # print (df)
        df.to_csv ( 'Optiq.csv' )
