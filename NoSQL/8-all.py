#!/usr/bin/env python3
""" """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ Python function that lists all documents in a collection: """
    list = []
    result = mongo_collection.find()
    if mongo_collection.count_documents({}) < 1:
        return list
    else:
        return result