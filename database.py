from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://bigbroqb:bigbrother@cluster0-shard-00-00-a4qe4.mongodb.net:27017,cluster0-shard-00-01-a4qe4.mongodb.net:27017,cluster0-shard-00-02-a4qe4.mongodb.net:27017/facebook?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.facebook
collection = db.users

def add_new_user(user):
	id = collection.insert_one(user).inserted_id
	print(id)
	return id

def main(user):
	add_new_user(user)

if __name__ == "__main__":
	test_user = {"_id": 123456789, "name": "Connor Hebert", "address": "123 Maple Street", "age": 21,  "date": datetime.datetime.utcnow()}
	main(test_user)