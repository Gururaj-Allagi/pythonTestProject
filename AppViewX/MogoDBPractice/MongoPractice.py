import pymongo
from pymongo import MongoClient


class testClass:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        print("init")

    def test_test(self):
        print("Guru")


def MongoDBConnectoion(self):
    cluster = MongoClient("mongodb+srv://root:root@cluster0.wxsvq.mongodb.net/test?retryWrites=true&w=majority")

    db = cluster["sample_analytics"]
    collection = db["accounts"]

    post = {"_id": 0, "Name": "Guru"}

    # collection.insert_one(post)

    res = collection.find({"account_id": 371138})

    for result in res:
        return result
