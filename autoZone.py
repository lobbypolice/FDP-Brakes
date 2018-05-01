import scrapy

class autoZone(scrapy.Spider):
    name = "autoZone"
    start_urls = ["https://www.autozone.com/brakes-and-traction-control/brake-pads",]

    def parse(self, reponse):
        #need to write rotating user agent or something
        #autoZone has got us MARKED 