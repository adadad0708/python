from bs4 import BeautifulSoup
import requests

def queryNewBalance():
    r = requests.get('https://holderm.com/')
    soup = BeautifulSoup(r.content, 'html.parser')
    dsfd = soup.find ( 'div', class_='product__thumbs' )
    print(dsfd)

    # image = soup.find('div', class_='slick-list').find_all("img")
    image = soup.find_all('img', class_='lazyloaded')
    print(image)
    num = 1
    for images in image:
        print ( images,"dse" )
        if ['data-src'] in images:
            print ( 'images',22 )

            images = (images['src'])
            images = "https:" + images
            images = images.replace ( '180', '720' )
            print ( images )

            # a = requests.get ( images )
            # with open ( r'E:\新品杂货\2022\0328\01\{}.jpg'.format ( num ), 'wb' ) as f:
            #     f.write ( a.content )  # 二进制
            #     num += 1

        else:
            print("rr")
            print ( images,"er" )

            images = (images['src'])
            images = "https:" + images
            images = images.replace ( '180', '720' )
            print ( images )


            a = requests.get ( images )
            with open ( r'E:\新品杂货\2022\0328\01\{}.jpg'.format ( num ), 'wb' ) as f:
                f.write ( a.content )  # 二进制
                num += 1
queryNewBalance()
