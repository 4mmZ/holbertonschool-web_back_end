#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['logs']
collection = db['nginx']

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

status_count = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\t{method}: {count} logs")

print(f"method=GET path=/status: {status_count} logs")

client.close()
