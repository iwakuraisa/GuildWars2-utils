from pymongo import MongoClient
import json

def get_connection_str():
	with open("settings/connection.json") as connection_file:
		connection = json.load(connection_file)
		connection_str = 'mongodb://{0}:{1}@{2}'.format(connection['user'],connection['password'],connection['domain']) 
		return connection_str

def gw2_db():
	client = MongoClient(get_connection_str())
	return client.gw2