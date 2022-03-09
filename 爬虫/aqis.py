import requests
from  lxml import  etree
import os

if __name__ == '__main__':
    # url
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers).text
    tree = etree.HTML(reponse)
    normal_li_List = reponse.tree('//div[@class="container"]//div[@class="all"]/div[2]/ul/div[2]/li')

    print ( normal_li_List )
    print(normal_li_List)
    for normal_li in normal_li_List:
        dateli = normal_li.xpath('./a/text()')
        print(dateli)