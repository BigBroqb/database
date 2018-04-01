from pymongo import MongoClient

client = MongoClient("mongodb://bigbroqb:bigbrother@cluster0-shard-00-00-a4qe4.mongodb.net:27017,cluster0-shard-00-01-a4qe4.mongodb.net:27017,cluster0-shard-00-02-a4qe4.mongodb.net:27017/facebook?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.facebook #defines database to use
users = db.users #defines collection within database to use

def add_user_data(user_data, id):
	"""Creates new user entry with specified id if user does not exist, otherwise updates existing user entry with specified id"""
	if get_user_data(id) == None:
		user_data["_id"] = id
		return users.insert_one(user_data).inserted_id
	else:
		return update_user_data(user_data, id)

def get_user_data(id):
	"""Given unique id, returns the existing entry for that user"""
	return users.find_one({"_id": id})

def remove_user_data(id):
	return users.delete_one({"_id": id})

def update_user_data(update, id):
	"""Helper method to update existing user entry"""
	return users.replace_one({"_id": id}, update)

def num_users():
	"""Returns the current number of existing user entries in the db"""
	return users.count()