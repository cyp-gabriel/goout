import scrapy
from goout_spider.items import GooutSpiderItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['goout.net']
    start_urls = ['https://goout.net/en/prague/events/leznyvlkk/']

    def parse(self, response):
        self.logger.info('In call to parse()')
        cards = response.css('div.schedule-box.small')
        for card in cards:
            item = GooutSpiderItem()
            item['title'] = str(card.css('div:first-child > a:first-of-type::text').get()).strip()
            item['time'] = card.css('div:nth-of-type(2) div.text-truncate > span > time::text').get().strip()
            yield item
