#!/usr/bin/env python3
""" """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ """
    list = []
    for x in mongo_collection.find():
        list.append(x)
    return list
