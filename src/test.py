from pymongo import MongoClient
from celery import Celery


def insert_item_one(mongo, data, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result


def insert_item_many(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


def main():
    host = "localhost"
    port = "27017"
    mongo = MongoClient(host, int(port), username='root', password='password')
    print(mongo)
    insert_item_one(mongo, {"text": "Hello Python222"}, "test_db", "test_col")


if __name__ == "__main__":
    main()
