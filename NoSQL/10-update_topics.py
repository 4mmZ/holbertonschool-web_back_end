#!/usr/bin/env python3
"""10. Change school topics"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a school document based on the name"""
    filter_query = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter_query, update_operation)
    return result
