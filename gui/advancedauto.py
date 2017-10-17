# -*- coding: utf-8 -*-
import scrapy

#scrapy runspider advanceauto.py -o quotes.json
class AdvancedautoSpider(scrapy.Spider):
    name = 'advancedauto'
    allowed_domains = ['https://shop.advanceautoparts.com/']
    start_urls = ['https://shop.advanceautoparts.com/p/carquest-wearever-gold-ceramic-brake-pads-rear-4-pad-set-gnad999/15520589-P?krypto=HCVk3prZ2zADyoZTi5uiLu2h8Cge2dE9tVuRRqgGR5IH9iujTFZv9pCVNaB6jP8DXaV%2Ft47fAaqrQ9dFn%2BO1ZqI3Jn41ZmhIL%2FMpRGOlCLpaNeW2B%2B%2FfbGhAkT1yoCI7tmcKWGb6lV%2B4%2FXTREBxNBa3s1XTJrM6gXjgoYzwp1iK%2FWGXZjorrmHvR4NsXIUQx',]

    def parse(self, response):
        yield{
            'title': response.xpath('//title/text()').extract(),
            'price': response.xpath('//*[@class="aap-productdetails-delivery__price"]//text()').extract()[1],
        }
           
            
