from flask import request, jsonify
from app.models import post_class as Posts
import pymongo
import copy

url = "mongodb://localhost:27017/"
db_name = "kenzie"
collection_name = "posts"
client = pymongo.MongoClient(url)
db = client[db_name]

def reading_posts():
    
    lists = db.collection_name.find().limit(10)

    print(lists)
