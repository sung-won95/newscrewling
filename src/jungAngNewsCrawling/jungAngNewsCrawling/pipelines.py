# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem

class JungangnewscrawlingPipeline:

    def __init__(self):
        host = "mongo"
        port = "27017"
        self.mongo = MongoClient(host, int(port), username='root', password='password')

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!". format(data))

        if valid:
            result = self.mongo["test_db"]["test_col"].insert_one(dict(item)).inserted_id

        return item
