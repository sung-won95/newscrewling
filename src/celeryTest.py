from pymongo import MongoClient
from celery import Celery
import datetime

swApp = Celery('newsCrewling', broker='pyamqp://guest@localhost//')


@swApp.task
def swMongoSave(data):
    host = "localhost"
    port = "27017"
    mongo = MongoClient(host, int(port), username='root', password='password')
    result = mongo["test_db"]["test_col"].insert_one(
        {"text": "afdsafHeadsfsadflloefefewfwef Pythoefefen222", "time": datetime.datetime.now(), "data": 'data'}).inserted_id
    return result
