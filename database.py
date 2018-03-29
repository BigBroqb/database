from pymongo import MongoClient
import datetime

if __name__ == "__main__":
	client = MongoClient("mongodb://bigbroqb:bigbrother@cluster0-shard-00-00-a4qe4.mongodb.net:27017,cluster0-shard-00-01-a4qe4.mongodb.net:27017,cluster0-shard-00-02-a4qe4.mongodb.net:27017/facebook?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
	db = client.facebook
	collection = db.users

	post = {"_id": 123456789, "author": "Joe", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

	def add_new_user(user):
		id = collection.insert_one(user).inserted_id
		print(id)


	add_new_user(post)