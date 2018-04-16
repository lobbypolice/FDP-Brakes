import scrapy

class advancedAuto(scrapy.Spider):
    name = "Autozone"
    start_urls = []
    

    def parse(self, response):
        for model in response.css('div.shelfItemDetails'):
            yield{
                'modelNumber': model.css('span').extract(),
                'type': model.css('li.prodNotes').extract(),
                'price': model.css('div.price').extract(), 
            }
            #aap-pl-js-itemlist > div:nth-child(1)
    def __init__(self):
        for i in range(1, 445):
            self.start_urls.append("https://www.autozone.com/brakes-and-traction-control/brake-pads?pageNumber=" + str(i))
#//*[@id="item_details_298604_0"]/ul/li[2]/em/span
#//*[@id="item_details_202573_1"]/ul/li[2]/em/span
#<span property="mpn">27111</span>