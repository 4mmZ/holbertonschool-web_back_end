#!/usr/bin/env python3
"""10. Change school topics"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """doc"""
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    return result
