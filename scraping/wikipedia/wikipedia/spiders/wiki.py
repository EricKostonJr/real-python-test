from scrapy import Spider
from scrapy.selector import Selector
from urllib.parse import urljoin

from wikipedia.items import WikipediaItem


class BasicSpider(Spider):
    # name the spider
    name = 'wiki'
    

    # allowed domains to scrape
    allowed_domains = ['en.wikipedia.org']

    # urls the spider begins to crawl from
    start_urls = (
        'http://en.wikipedia.org/wiki/Category:2016_films',
    )

    # parses and returns the scraped data
    def parse(self, response):
        
        titles = Selector(response).xpath('//div[@id="mw-pages"]//li')

        for title in titles:
            item = WikipediaItem()
            url = title.xpath("a/@href").extract()
            if url:
                item['title'] = title.xpath("a/text()").extract()
                item['url'] = urljoin('http://en.wikipedia.org', url[0])
                yield item