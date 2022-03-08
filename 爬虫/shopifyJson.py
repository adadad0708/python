from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

wassersteinweb = []
for x in range ( 1, 10 ):
    # URL = 'https://wusire.com/collections/tops/products/blue-cotton-blend-crew-neck-floral-casual-shirts-tops.json'
    URL = 'https://www.meomaker.com/collections/magic-technology-products/products.json?limit=250&page='
    productWeb = requests.get ( URL + str ( x ) )

    # productWeb = requests.get(URL)

    ProductData = productWeb.json ()
    for item in ProductData['products']:
        try:
            title = (item['title'])
        except Exception as e:
            title = None
        try:
            body_html = (item['body_html'])
        except Exception as e:
            body_html = None
        try:
            created = (item['created_at'])
        except Exception as e:
            created = None
        try:
            vendor = (item['vendor'])
        except Exception as e:
            vendor = None
        try:
            handle = (item['handle'])
        except Exception as e:
            handle = None
        try:
            tags = (item['tags'])
        except Exception as e:
            tags = None
        try:
            productType = (item['product_type'])
        except Exception as e:
            productType = None
        for images in item['images']:
            # print(images)
            try:
                images = (images['src'])
            except Exception as e:
                images = None
            # try:
            #     position = (images['position'])
            #     print (position)
            # except Exception as e:
        for i in range ( 5 ):
            for option in item['options']:
                    print(option)
                    try:
                        optionA = (option['name'])
                        print (option, "A")
                    except Exception as e:
                        optionA = None
                    try:
                        optionB = (option['name'])
                        print (optionB, "B")
                    except Exception as e:
                        optionB = None
                    try:
                        optionC = (option['name'])
                    except Exception as e:
                        optionC = None

        for variant in item['variants']:
            # print(variant)

            try:
                variants_title = (variant['title'])
            except Exception as e:
                variants_title = None
            try:
                option1 = (variant['option1'])
            except Exception as e:
                option1 = None
            try:
                option2 = (variant['option2'])

            except Exception as e:
                option2 = None
            try:
                option3 = (variant['option1'])
            except Exception as e:
                option3 = None
            try:
                SKU_ = (variant['sku '])
            except Exception as e:
                SKU = None
            try:
                variantPrice = (variant['price'])
            except Exception as e:
                variantPrice = None
            try:
                variantComparePrice = (variant['compare_at_price'])
            except Exception as e:
                variantComparePrice = None
            element_info = {
                'Title': title,
                'Body (HTML)': body_html,
                'Created at': created,
                'Vendor': vendor,
                'Tags': tags,
                'URL': handle,
                'Product Type': productType,
                'variants_title': variants_title,
                'Price': variantPrice,
                'Compare Price': variantComparePrice,
                'SKU': SKU,
                'Image Src': images,

            }

            wassersteinweb.append ( element_info )
            # print ( wassersteinweb )

df = pd.DataFrame ( wassersteinweb )
# print (df)
df.to_csv ('dmeqqwwodmb.csv')
