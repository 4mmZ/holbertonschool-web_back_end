#!/usr/bin/env python3
"""10. Change school topics"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a school document based on the name"""
    options = {}
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}}, **options)
    return result
