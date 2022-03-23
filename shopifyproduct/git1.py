import re
import os
import scrapy
import json
import csv

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['thetrailerpartsoutlet.com', 'node1.itoris.com']
    start_urls = ['http://thetrailerpartsoutlet.com/']

    def helperExtractor(self, dom, xpath):
        text = re.sub(r"\s+", " ", "\n".join(dom.xpath(xpath).extract()))
        return text.strip() if text else ""

    def write_csv(self, item):
        file_exists = os.path.exists(self.result_file)
        with open(self.result_file, "a", encoding="utf-8-sig", newline="") as result_f:
            fieldnames = item.keys()
            writer = csv.DictWriter(result_f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(item)

    def parse(self, response):
        categories = response.xpath(
            '//div[@class="desktop-menu"]//div[@class="dropdown-content"]/ul/li/a/@href'
        ).extract()
        for category in categories:
            cateogory_link = f'http://thetrailerpartsoutlet.com{category}'
            yield scrapy.Request(cateogory_link, callback=self.parse_products)

    def parse_products(self, response):
        products = response.xpath('//a[contains(@class, "grid-view-item__link")]/@href').extract()
        for product in products:
            product_link = f'http://thetrailerpartsoutlet.com{product}'
            yield scrapy.Request(product_link, callback=self.parse_detail)

        pagination = response.xpath('//ul[contains(@class, "pagination")]/li[last()]/a/@href').get()
        if pagination:
            pagination_link = f'http://thetrailerpartsoutlet.com{pagination}'
            yield scrapy.Request(pagination_link, callback=self.parse_products)

    def parse_detail(self, response):
        product_container = response.xpath('//div[contains(@class, "product-template__container")]')
        item = dict()

        item["id"] = self.helperExtractor(product_container, './/p[@class="product-single__sku"]/span//text()')
        item["title"] = self.helperExtractor(product_container, './/h1[@class="product-single__title"]//text()')
        item["description"] = self.helperExtractor(product_container, './/div[contains(@class, "product-single__description")]//text()')
        item["price"] = self.helperExtractor(product_container, './/span[@id="ProductPrice-product-template"]//text()')
        item["link"] = response.url
        item["image_link"] = self.helperExtractor(product_container, './/meta[@itemprop="image"]//@content')

        response_text = response.text
        product_text = response_text.split("window.wn.product")[1].split("window.wn.")[0].strip(" \n;=").replace("\n", "")
        variant_text = product_text.split("variants:")[1].rsplit("]", 1)[0]+"]"
        variant_json = json.loads(variant_text)
        availability = variant_json[0]["available"]
        item["availability"] = "In stock" if availability else "Out stock"
        item["brand"] = ""

        if len(variant_json) > 1:
            try:
                product_id = product_text.split("id:")[1].split(",")[0].strip()
                variant_id = variant_json[0]["id"]
            except:
                product_id = self.helperExtractor(product_container, './/h1[@class="product-single__title"]/following-sibling::div/@data-product-id')
                variant_id = self.helperExtractor(product_container, './/select[@id="ProductSelect-product-template"]/option[@selected="selected"]/@value')

            data = {
                'product_id': str(product_id),
                'variant_id': str(variant_id),
                'customer_id': '0',
                'template_id': '0',
                'skip_assoc_data_check': '0'
            }

            link = 'https://node1.itoris.com/dpo/storefront/include.js?controller=GetOptionConfig&shop=the-trailer-parts-outlet.myshopify.com'
            yield scrapy.FormRequest(link, formdata=data, callback=self.parse_brand, meta={"item": item})
        else:
            yield item
            self.write_csv(item)

    def parse_brand(self, response):
        item = response.meta["item"]
        label = response.xpath('//label[@class="required"][contains(text(), "Brand")]')
        if label:
            brands = label.xpath('./following-sibling::div//label[contains(@class, "admin__field-label")]/span[1]')
            brandss = [self.helperExtractor(brand, './/text()') for brand in brands]
            item["brand"] = brandss

        yield item
        self.write_csv(item)