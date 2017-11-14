import scrapy

class advancedAuto(scrapy.Spider):
    name = "advancedAuto"
    start_urls = ["https://shop.advanceautoparts.com/web/PartSearchCmd?storeId=10151&catalogId=10051&pageId=partTypeList&suggestion=&actionSrc=Form&langId=-1&categoryId=15694&beginIndex=0&sortBy=5&_r=0.8193827588178413#",]
    

    def parse(self, response):
        for model in response.css('div.aap-pl-item'):
            yield{
                'modelNumber': model.css('span.aap-pl-item__prno::text').extract_first(),
                'name': model.css('h3.aap-pl-item__pname::text').extract_first(),
                'price': model.css('span.aap-pl-item__price::text').extract_first(), 
            }
