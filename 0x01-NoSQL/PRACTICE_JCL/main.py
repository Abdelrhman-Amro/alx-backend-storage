#!/usr/bin/env python3

import os
from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values

load_dotenv()

connection_string = os.getenv('MONGO_CONNECTION_STRING')
client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)
learn_Mongo_DB = client.learn_Mongo_DB
collections = learn_Mongo_DB.list_collection_names()
print(collections)
