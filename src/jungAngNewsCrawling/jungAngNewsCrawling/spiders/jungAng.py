import scrapy
from jungAngNewsCrawling.items import JungangnewscrawlingItem


class JungangSpider(scrapy.Spider):
    name = 'jungAng'
    allowed_domains = ['https://news.joins.com/money/finance/list?cloc=joongang-section-subsection']
    start_urls = ['https://news.joins.com/money/finance/list?cloc=joongang-section-subsection']

    def parse(self, response):
        for column in response.xpath('//*[@id="content"]/div[2]/ul/li'):
            item = JungangnewscrawlingItem()

            item['title'] = column.xpath('h2/a/text()').extract()[0]
            item['url'] = 'https://news.joins.com' + column.xpath('h2/a/@href').extract()[0]

            yield item
