import scrapy
import csv

class napa(scrapy.Spider):
    name = "oreilly"
    start_urls = []

    def __init__(self):
        writer = []
        with open('reilly.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    writer.append(row)
        for x in writer:
            x = x[2:-2]
            self.start_urls.append("https://www.napaonline.com/en/search?q=" + x)
    def parse(self, response):
        for model in response.css('div.product-container'):
            yield{
                'modelNumber' : model.css( 'dd.item-number:text').extract_first(),
                'name' : model.css('a.js-product-link::text').extract_first(),
                'material' : model.xpath('//*[contains(@class,\'attribute_wrap\')]/span/strong/text()').extract_first(),
            }
            #productListItemADOAD7822_203472555 > div.listing-content > div.listing-detail > div.listing-detail-item.listing-detail-item-part > div.listing-detail-text.listing-detail-text-par
            #productListItemADOAD7822_203472555 > div.listing-aside > div.listing-price-wrap > div.listing-price-block > div.listing-price > div.listing-price-amount > span.listing-price-value
            #productTitle