import scrapy
from ..items import GoodreadsItem
from scrapy import Request
from urllib.parse import urljoin
from urllib.parse import urlparse


class CrawlnscrapeSpider(scrapy.Spider):
    name = 'crawlNscrape'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/list/show/702.Cozy_Mystery_Series_First_Book_of_a_Series']

    def parse(self, response):
 
        for href in response.xpath("//tbody[@id='booksBody']/tr"):
            url=response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.xpath("(//a[@class='next_page'])[1]/@href")
        if next_page:
            url= response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
        
        
            

    def parse_page(self, response):
        book = GoodreadsItem()
        title = response.xpath("td[@class='field title']/div/a/text()").extract_first().strip()


        book['title'] = title
        
        yield book
