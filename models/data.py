from pymongo import MongoClient
from bson.objectid import ObjectId
mongo_uri = "mongodb+srv://admin:admin@cluster0-kb7pi.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)
cafe_app = client.Cafeshop
cafe_ndt = cafe_app["cafes"]
