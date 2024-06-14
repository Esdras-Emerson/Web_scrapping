import scrapy 

class quotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/',
       
    ]

    def parse(self, response):
        page = response.xpath('*//div[@class="quote"]')
        for quote in page:
           yield {
                'title' : quote.xpath('.//span[@class="text"]/text()').get(),
                'author' : quote.xpath('.//small[@class="author"]/text()').get(),
                'tags' : quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()

            }

        next_page = response.xpath('*//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)