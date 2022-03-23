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
    i = 0
    title= soup2.find ( "h1", {"class": "product-single__title"} ).get_text().strip()
    price= soup2.find ( "span", {"class": "money"} ).get_text().replace("$", "").strip()



    optionA = soup2.find ( "label", {"for": "ProductSelect--product-template-option-0"} ).text.strip()

    optionAval = soup2.find ( "fieldset", {"id": "ProductSelect--product-template-option-0"} ).find ( "label" ).text.strip()
    if optionAval:
        # optionAval = optionAval
        print ( optionAval, "optionAval" )
        # for optionAval in optionAval:
        #     print ( optionAval, "optionAval" )
            # element_info2 = {
            #
            # }
            # wassersteinweb.append ( element_info2 )

    optionB = soup2.find ( "label", {"for": "ProductSelect--product-template-option-1"} ).text.strip()

    optionBval = soup2.find ( "fieldset", {"id": "ProductSelect--product-template-option-1"} ).find_all ("label" )

    if optionB:

        for optionBval in optionBval:
            optionBval = optionBval.text
            print ( optionBval, "optionBval" )


    imga = soup2.find ( "div", {"class": "product-single__thumbnails"} )
    if imga:

        img = imga.find_all ( "img" )
        print(img,"img")
        for img in img:
            img = img["src"]
            img = "https:" + img
            img = img.replace ( '150', '720' )
            i+=1;



            element_info = {
                'Handle': handle,
                'Title': title,
                'Vendor': 'NEW-202203211',
                'Tags': 'Dress',

                'Variant Price': price,
                'Variant Compare At Price': price,
                'Option1 Value': optionA,
                'Option1 Name': optionAval,
                'Option2 Value': optionB,
                'Option2 Name': optionBval,
                'Image Src': img,
                'Image Position': i,

            }

            wassersteinweb.append ( element_info )

    else:
        img = soup2.find ( "img", {"class": "product-single__photo"} )
        print(img,"izoomImgg")

        img = img["src"]
        img = "https:" + img
    df = pd.DataFrame ( wassersteinweb )
    # print (df)
    df.to_csv ('44.csv')
    df.to_csv ('44.csv')





