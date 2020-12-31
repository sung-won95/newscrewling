import scrapy
import re
from jungAngNewsCrawling.items import JungangnewscrawlingItem
from konlpy.tag import Hannanum

class JungangSpider(scrapy.Spider):
    name = 'jungAng'
    allowed_domains = ['https://news.joins.com/money/finance/list?cloc=joongang-section-subsection']
    start_urls = ['https://news.joins.com/money/finance/list?cloc=joongang-section-subsection']

    def parse(self, response):
        hannanum = Hannanum()
        for column in response.xpath('//*[@id="content"]/div[2]/ul/li'):
            item = JungangnewscrawlingItem()

            item['title'] = column.xpath('h2/a/text()').extract()[0]
            item['url'] = 'https://news.joins.com' + column.xpath('h2/a/@href').extract()[0]
            item['keyword'] = hannanum.nouns(re.sub(pattern='[^\w\s\\%]',repl=' ',string = item["title"]))
            print(re.search(pattern='((\d{1,5}(~|.)\d{1,5}|\d{1,5})(%|)|)',string = item["title"]))

            yield item
